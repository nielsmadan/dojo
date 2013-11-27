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

function printValue(fn) {
    console.log(fn);
    return fn;
}

function multiplyBy2(num) {
    return num * 2;
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
    it('', function(){
      var two = church.increment(church.increment(church.zero));
      assert.equal(two(multiplyBy2(1), 4);
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
    it('', function(){
      var x = 0;
      var counter = function (fn) {
            x += 1;
            return fn;
      }

      var three = church.increment(church.increment(church.increment(church.zero)));

      church.unwind(three, counter);
      assert.equal(x, 3);
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
    it('', function(){
      var two = church.increment(church.increment(church.zero));
      var three = church.increment(church.increment(church.increment(church.zero)));

      var five = church.add(two, three);
      assert.equal(five(printBar)(null), null);
    });
});

describe('mul', function() {
    it('', function(){
      var ci = church.increment;
      var x = 0;
      var counter = function (fn) {
            x += 1;
            return fn;
      }

      var five = ci(ci(ci(ci(ci(church.zero)))));
      var three = church.increment(church.increment(church.increment(church.zero)));

      var fifteen = church.mul(five, three);

      church.unwind(fifteen, counter);
      assert.equal(x, 15);
    });
    it('', function(){
      var ci = church.increment;
      var five = ci(ci(ci(ci(ci(church.zero)))));
      var three = church.increment(church.increment(church.increment(church.zero)));

      var fifteen = church.mul(five, three);

      assert.equal(fifteen(printBar)(null), null);
    });
});
