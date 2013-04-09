var pn = require('./phone_numbers');
var assert = require("assert")

describe('square', function(){
    it('should return 25 when the argument is 5', function(){
      assert.equal(pn.square(5), 25);
    })
})
