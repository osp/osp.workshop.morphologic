#!/usr/bin/ruby

file = "motion-size.ps"
x = 80
y = 80
text = "fuck it"
n = 1

# directory setup
fullpath = File.expand_path(__FILE__)
dir = File.dirname(fullpath)

(1..72).each do |n|
	ps = "/fontsize #{n} def
	/headerfont /Courier findfont fontsize scalefont def
	headerfont setfont

	#{x} #{y} moveto
	(#{text}) show"

	Dir.chdir("#{dir}/tmp-size")
	f = File.open(file, 'w')
	f.puts ps
	f.close

	cmd = Thread.new do
		%x[convert #{file} motion-length-#{n}.png]
	end
	cmd.join
end
