io.write('input the numbers you want the sum of : ')
local input = io.read()

input = string.gsub(input, "%.", "")

local function calculate(...)
    local array = {...}
    for i = 1, #array do
        for v in array[i]:gmatch(".")do
            if v == ',' or v == '+' then
                print(v)
                string.gsub(array[1], ',', '')
            end
        end
    end
    local result = 0
    for i = 1, #array do
        print(array[1])
        result = result + tonumber(array[1])
    end
    return result
end

print(calculate(input))
