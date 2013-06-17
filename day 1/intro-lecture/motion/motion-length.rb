#!/usr/bin/ruby

file = "motion-length.ps"
x = 80
y = 80
text = "morphologic"

# directory setup
fullpath = File.expand_path(__FILE__)
dir = File.dirname(fullpath)

(1..text.length).each do |n|
	ps = "/fontsize 64 def
	/headerfont /Courier findfont fontsize scalefont def
	headerfont setfont

	#{x+n*20} #{y} moveto
	(#{text[n-1]}) show"

	Dir.chdir("#{dir}/tmp")
	f = File.open(file, 'w')
	f.puts ps
	f.close

	cmd = Thread.new do
		%x[convert #{file} motion-length-#{n}.png]
	end
	cmd.join
end
