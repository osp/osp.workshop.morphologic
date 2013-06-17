A simple script combining different techniques of procedural
image generation.

Using the Ruby scripting language we generate snippets of
the PostScript vector language, which we convert into pngs
by feeding them to the ImageMagick command (called `convert`).

Because we change certain variables every time we generate
the PostScripts, the illusion of motion is created.

