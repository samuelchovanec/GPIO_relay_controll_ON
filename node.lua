gl.setup(NATIVE_WIDTH, NATIVE_HEIGHT)

local font = resource.load_font "font.ttf"

function node.render()
    font:write(250, 300, "Hello world", 64, 1,1,1,1)
    gl.clear(0, 1, 0, 1) -- green
 
end
end
