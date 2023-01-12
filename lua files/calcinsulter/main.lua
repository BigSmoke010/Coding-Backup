local json = require('JSON')

local insultsjson = io.open('./insults.json', 'r')
local jsoninsults = json:decode(insultsjson:read('a'))
insultsjson:close('./insults.json')

local complimentsjson = io.open('./compliments.json', 'r')
local jsoncompliments = json:decode(complimentsjson:read('a'))
complimentsjson:close('./compliments.json')

math.randomseed(os.time())
x, y = math.random(0, 100), math.random(0, 100)

io.write('whats ' .. x .. ' + ' .. y .. ': ')
answer = io.read()

while answer ~= 'q' do
    if tonumber(answer) == x + y then
        print(jsoncompliments['anytime'][math.random(#jsoncompliments['anytime'])])
        print('correct')
        x, y = math.random(0, 100), math.random(0, 100)
        io.write('whats'.. x ..' + ' .. y .. ': ') 
        answer = io.read()
    else
        print(jsoninsults[math.random(#jsoninsults)])
        print('wrong')
        x, y = math.random(0, 100), math.random(0, 100)
        io.write('whats'.. x ..' + ' .. y .. ': ') 
        answer = io.read()
    end
end

