module Jekyll

  class TagIndex < Page
    def initialize(site, base, dir, tag)
      @site = site
      @base = base
      @dir = dir
      @name = 'index.html'
      self.process(@name)
      self.read_yaml(File.join(base, '_layouts'), 'tag_index.html')
      self.data['tag'] = tag

      self.data['related'] = []
      site.tags[tag].each do |post|
        post.tags.each do |rel| 
          self.data['related'].push(rel)
        end
      end
      self.data['related'] = self.data['related'].uniq

      tag_title_prefix = site.config['tag_title_prefix'] || 'Tag: '
      self.data['title'] = "#{tag_title_prefix}#{tag}"
    end
  end

  class TagFeed < Page
    def initialize(site, base, dir, tag)
      @site = site
      @base = base
      @dir = dir
      @name = 'atom.xml'

      self.process(@name)
      self.read_yaml(File.join(base, '_layouts'), 'tag_feed.xml')
      self.data['tag'] = tag
      tag_title_prefix = site.config['tag_title_prefix'] || 'Tag: '
      self.data['title'] = "#{tag_title_prefix}#{tag}"
    end
  end

  #class TagList < Page
  #  def initialize(site,  base, dir, tags)
  #    @site = site
  #    @base = base
  #    @dir = dir
  #    @name = 'index.html'
  #
  #    self.process(@name)
  #    self.read_yaml(File.join(base, '_layouts'), 'tag_list.html')
  #    self.data['tags'] = tags
  #  end
  #end

  class TagGenerator < Generator
    safe true
    
    def generate(site)
      if site.layouts.key? 'tag_index'
        dir = site.config['tag_dir'] || 'tags'
        site.tags.keys.each do |tag|
          write_tag_index(site, File.join(dir, tag.gsub(/\s/, "-").gsub(/[^\w-]/, '').downcase), tag)
        end
      end

      if site.layouts.key? 'tag_feed'
        dir = site.config['tag_dir'] || 'tags'
        site.tags.keys.each do |tag|
          write_tag_feed(site, File.join(dir, tag.gsub(/\s/, "-").gsub(/[^\w-]/, '').downcase), tag)
        end
      end

      #if site.layouts.key? 'tag_list'
      #  dir = site.config['tag_dir'] || 'tags'
      #  write_tag_list(site, dir, site.tags.keys.sort)
      #end
    end
  
    def write_tag_index(site, dir, tag)
      index = TagIndex.new(site, site.source, dir, tag)
      index.render(site.layouts, site.site_payload)
      index.write(site.dest)
      site.static_files << index
    end
  
    def write_tag_feed(site, dir, tag)
      index = TagFeed.new(site, site.source, dir, tag)
      index.render(site.layouts, site.site_payload)
      index.write(site.dest)
      site.static_files << index
    end

    #def write_tag_list(site, dir, tags)
    #  index = TagList.new(site, site.source, dir, tags)
    #  index.render(site.layouts, site.site_payload)
    #  index.write(site.dest)
    #  site.static_files << index
    #end
  end

end
