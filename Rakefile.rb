##############
# Jekyll tasks
##############

# Usage: rake serve, rake serve:prod
task :serve => ["serve:dev"]
namespace :serve do

  desc "Serve development Jekyll site locally"
  task :dev do
    puts "Starting up development Jekyll site server..."
    system "JEKYLL_ENV=development bundle exec jekyll serve --incremental --config _config.yml,_config.dev.yml --host=0.0.0.0"
  end

  desc "Serve production Jekyll site locally"
  task :prod do
    puts "Starting up production Jekyll site server..."
    system "JEKYLL_ENV=production bundle exec jekyll serve --no-watch"
  end
end

# Usage: rake build, rake build:dev, rake build:drafts
task :build => ["build:prod"]
namespace :build do

  desc "Regenerate files for production"
  task :prod do
    puts "* Regenerating files for production..."
    system "JEKYLL_ENV=production bundle exec jekyll build"
  end

  desc "Regenerate files for development"
  task :dev do
    puts "* Regenerating files for development..."
    system "bundle exec jekyll build --config _config.yml,_config.dev.yml --profile"
  end

  desc "Regenerate files and drafts for development"
  task :drafts do
    puts "* Regenerating files and drafts for development..."
    system "bundle exec jekyll build --config _config.yml,_config.dev.yml --profile --drafts"
  end
end

####################
# Notification tasks
####################

# Usage: rake notify
task :notify => ["notify:pingomatic", "notify:google", "notify:bing"]
desc "Notify various services that the site has been updated"
namespace :notify do

  desc "Notify Ping-O-Matic"
  task :pingomatic do
    begin
      require 'xmlrpc/client'
      puts "* Notifying Ping-O-Matic that the site has updated"
      XMLRPC::Client.new('rpc.pingomatic.com', '/').call('weblogUpdates.extendedPing', 'Elbsides' , 'https://www.elbsides.de', 'https://www.elbsides.de/feed.xml')
    rescue LoadError
      puts "! Could not ping ping-o-matic, because XMLRPC::Client could not be found."
    end
  end

  desc "Notify Google of updated sitemap"
  task :google do
    begin
      require 'net/http'
      require 'uri'
      puts "* Notifying Google that the site has updated"
      Net::HTTP.get('www.google.com', '/webmasters/tools/ping?sitemap=' + URI.escape('https://www.elbsides.de/sitemap.xml'))
    rescue LoadError
      puts "! Could not ping Google about our sitemap, because Net::HTTP or URI could not be found."
    end
  end

  desc "Notify Bing of updated sitemap"
  task :bing do
    begin
      require 'net/http'
      require 'uri'
      puts '* Notifying Bing that the site has updated'
      Net::HTTP.get('www.bing.com', '/webmaster/ping.aspx?siteMap=' + URI.escape('https://www.elbsides.de/sitemap.xml'))
    rescue LoadError
      puts "! Could not ping Bing about our sitemap, because Net::HTTP or URI could not be found."
    end
  end
end

####################
# Cache clearing
####################

# Usage: rake notify
task :clearcache => ["clearcache:cloudfront"]
desc "Clear caches"
namespace :clearcache do
  desc "Clear Cloudfront cache"
  task :cloudfront do
    begin
      system "aws cloudfront create-invalidation --distribution-id ERQ04IADGK5U0 --paths \"/*\""
    end
  end
end

###############
# Testing tasks
###############

task :test do
  require 'html-proofer'
  sh "bundle exec jekyll build"
  options = { :empty_alt_ignore => true }
  HTMLProofer.check_directory("./_site", options).run
end

##################
# Deployment tasks
##################

# Usage: rake s3_website
desc "push the contents of ./_site to S3"
task :s3_website do
  puts "* syncing the contents of ./_site to the server"
  #system "s3_website push" # use --force with S3 config updates
  system "aws s3 sync _site/ s3://elbsides.de/ --delete --exclude \".DS_Store\" --exclude \".yml\" "
end

# Usage: rake deploy
task :deploy => ["deploy:prod"]
namespace :deploy do
  desc "Regenerate and sync production files, and notify services of the update"
  # task :prod => ["build", "s3_website", "notify"] do
  task :prod => ["build", "s3_website", "clearcache"] do
  end
end
