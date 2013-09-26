var church = require('./church_numerals');
var assert = require("assert")

describe('zero', function() {
    it('should return a function that returns its input', function(){
      assert.equal(church.zero(undefined)(null), null);
    });
});

function printBar(fn) {
    console.log("|");
    return fn;
}

describe('increment', function() {
    it('', function(){
      var one = church.increment(church.zero);
      assert.equal(one(printBar)(null), null);
    });
    it('', function(){
      var two = church.increment(church.increment(church.zero));
      assert.equal(two(printBar)(null), null);
    });
});

describe('unwind', function() {
    it('', function(){
      var x = 0;
      var counter = function (fn) {
            x += 1;
            return fn;
      }

      var two = church.increment(church.increment(church.zero));

      church.unwind(two, counter);
      assert.equal(x, 2);
    });
});

describe('add', function() {
    it('', function(){
      var x = 0;
      var counter = function (fn) {
            x += 1;
            return fn;
      }

      var two = church.increment(church.increment(church.zero));
      var three = church.increment(church.increment(church.increment(church.zero)));

      var five = church.add(two, three);

      church.unwind(five, counter);
      assert.equal(x, 5);
    });
});
