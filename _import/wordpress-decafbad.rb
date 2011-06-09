require 'rubygems'
require 'sequel'
require 'fileutils'
require 'yaml'

# NOTE: This converter requires Sequel and the MySQL gems.
# The MySQL gem can be difficult to install on OS X. Once you have MySQL
# installed, running the following commands should work:
# $ sudo gem install sequel
# $ sudo gem install mysql -- --with-mysql-config=/usr/local/mysql/bin/mysql_config

# $ export DB=my_wpdb
# $ export USER=dbuser 
# $ export PASS=dbpass 
# $ ruby -r './_import/wordpress-decafbad.rb' -e 'Jekyll::WordPress.process( "#{ENV["DB"]}", "#{ENV["USER"]}", "#{ENV["PASS"]}" )'

module Jekyll
  module WordPress

    table_prefix = "wp_decafbad_"

    # Reads a MySQL database via Sequel and creates a post file for each
    # post in wp_decafbad_posts that has post_status = 'publish'.
    # This restriction is made because 'draft' posts are not guaranteed to
    # have valid dates.
    QUERY = <<-EOS
        SELECT 
            GROUP_CONCAT(#{table_prefix}terms.name SEPARATOR ",") as post_tags,
            post_title, post_name, post_date, post_content, post_excerpt, ID, guid
        FROM 
            #{table_prefix}posts
        LEFT JOIN
            (#{table_prefix}term_relationships, #{table_prefix}term_taxonomy, #{table_prefix}terms)
            ON 
            #{table_prefix}term_relationships.object_id=#{table_prefix}posts.id
            AND
            #{table_prefix}term_taxonomy.term_taxonomy_id=#{table_prefix}term_relationships.term_taxonomy_id
            AND
            #{table_prefix}terms.term_id=#{table_prefix}term_taxonomy.term_id
        WHERE 
            post_status = 'publish' AND 
            post_type = 'post'
        GROUP BY #{table_prefix}posts.id
    EOS

    def self.process(dbname, user, pass, host = 'localhost')
      db = Sequel.mysql(dbname, :user => user, :password => pass, :host => host, :encoding => 'utf8')

      FileUtils.mkdir_p "_posts"

      db[QUERY].each do |post|
        # Get required fields and construct Jekyll compatible name
        title = post[:post_title]
        slug = post[:post_name]
        date = post[:post_date]
        content = post[:post_content]
        name = "%02d-%02d-%02d-%s.markdown" % [date.year, date.month, date.day,
                                               slug]

        # Get the relevant fields as a hash, delete empty fields and convert
        # to YAML for the header
        data = {
           'layout' => 'post',
           'title' => title.to_s,
           'excerpt' => post[:post_excerpt].to_s,
           'tags' => post[:post_tags].nil? ? nil : post[:post_tags].split(','),
           'date' => post[:post_date].iso8601,
           'wordpress_slug' => post[:post_name],
           'wordpress_id' => post[:ID],
           'wordpress_url' => post[:guid]
         }.delete_if { |k,v| v.nil? || v == ''}.to_yaml

        # Write out the data and content to file
        File.open("_posts/#{name}", "w") do |f|
          f.puts data
          f.puts "---"
          f.puts content
        end
      end

    end
  end
end
