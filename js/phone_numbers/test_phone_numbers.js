var pn = require('./phone_numbers');
var assert = require("assert")

describe('startsWith', function() {
    it('should return true when the first argument is "1" and the second is also "1"', function(){
      assert.equal(pn.startsWith("1", "1"), true);
    });
    it('should return false when the first argument is "1" and the second is also "2"', function(){      
    	assert.equal(pn.startsWith("1", "2"), false);
    });
    it('should return false when the first argument is "1" and the second is also "12"', function(){      
    	assert.equal(pn.startsWith("1", "12"), false);
    });
    it('should return true when the first argument is "12" and the second is also "1"', function(){      
    	assert.equal(pn.startsWith("12", "1"), true);
    });
    it('should return true when the first argument is "12" and the second is also "1"', function(){      
    	assert.equal(pn.startsWith("12", ""), true);
    });
});

describe('isValidPhoneNumber', function() {
    it('should return true when the argument is "1"', function(){
      assert.equal(pn.isValidPhoneNumber("1"), true);
    });

    it('should return true when the argument is "12"', function(){
      assert.equal(pn.isValidPhoneNumber("12"), true);
    });

    it('should return false when the argument is "1a"', function(){
      assert.equal(pn.isValidPhoneNumber("1a"), false);
    });
});


describe('isConsistentNumberList', function() {
    it('should return true when the argument is ["1", "2"]', function(){
      assert.equal(pn.isConsistentNumberList(["1", "2"]), true);
    });
    it('should return false when the argument is ["12", "2","1"]', function(){
      assert.equal(pn.isConsistentNumberList(["12", "2", "1"]), false);
    });
    it('should return false when the argument is ["1", "2","12"]', function(){
      assert.equal(pn.isConsistentNumberList(["1", "2", "12"]), false);
    });
    // it('should return false when the argument is every number from 10000 to 29999', function(){
    //   var allNums = []
    //   for (var i = 10000; i < 30000; ++i) {
    //         allNums.push(i.toString());
    //   }
    //   assert.equal(pn.isConsistentNumberList(allNums), true);
    // });
});


describe('getEmptyPartitionedList', function() {
	it('should return [[], [], [], [], [], [], [], [], [], []]', function(){
      assert.deepEqual(pn.getEmptyPartitionedList(), [[], [], [], [], [], [], [], [], [], []]);
    });
});

describe('partitionList', function() {
	it('should return [["1"], ["2"], ["3"]] when the argument is ["1", "2", "3"]', function(){
      assert.deepEqual(pn.partitionList(["1", "2", "3"]), [["1"], ["2"], ["3"]]);
    });
  it('should return [["12", "13"], ["3"]] when the argument is ["12", "13", "3"]', function(){
      assert.deepEqual(pn.partitionList(["12", "13", "3"]), [["12", "13"], ["3"]]);
    });
  it('', function(){
      assert.deepEqual(pn.partitionList(["12", "13", "121","3"]),
                                        [["12", "13", "121"], ["3"]]);
    });
});

describe('removeFirstDigit', function() {
  it('', function(){
      assert.deepEqual(pn.removeFirstDigit([""]), [""]);
    });
  it('', function(){
      assert.deepEqual(pn.removeFirstDigit(["1"]), [""]);
    });
  it('', function(){
      assert.deepEqual(pn.removeFirstDigit(["12"]), ["2"]);
    });
  it('', function(){
      assert.deepEqual(pn.removeFirstDigit(["123456"]), ["23456"]);
    });
  it('', function(){
      assert.deepEqual(pn.removeFirstDigit(["12", "23"]), ["2", "3"]);
    });
  it('', function(){
      assert.deepEqual(pn.removeFirstDigit(["12", "23456", "1"]), ["2", "3456", ""]);
    });
});

describe('partitionExhausted', function() {
  it('', function(){
      assert.equal(pn.partitionExhausted(["1"]), false);
    });
  it('', function(){
      assert.equal(pn.partitionExhausted(["1", "2"]), false);
    });
  it('', function(){
      assert.equal(pn.partitionExhausted(["1", ""]), true);
    });
  it('', function(){
      assert.equal(pn.partitionExhausted([""]), false);
    });
});

describe('isConsistentNumberListPartioned', function() {
    it('should return true when the argument is ["1"]', function(){
      assert.equal(pn.isConsistentNumberListPartioned(["1"]), true);
    });
    it('should return true when the argument is ["1", "12"]', function(){
      assert.equal(pn.isConsistentNumberListPartioned(["1", "12"]), false);
    });
    it('should return true when the argument is ["11", "112"]', function(){
      assert.equal(pn.isConsistentNumberListPartioned(["11", "112"]), false);
    });
    it('should return true when the argument is ["91125426", "97625992", "911"]', function(){
      assert.equal(pn.isConsistentNumberListPartioned(["91125426", "97625992", "911"]), false);
    });
    it('should return true when the argument is ["91125426", "97625992", "912"]', function(){
      assert.equal(pn.isConsistentNumberListPartioned(["91125426", "97625992", "912"]), true);
    });
    // it('should return false when the argument is every number from 10000 to 29999', function(){
    //   var allNums = []
    //   for (var i = 10000; i < 30000; ++i) {
    //         allNums.push(i.toString());
    //   }
    //   assert.equal(pn.isConsistentNumberListPartioned(allNums), true);
    // });
    it('should return false when the argument is every number from 1000000 to 3000000', function(){
      var allNums = []
      for (var i = 1000000; i < 3000000; ++i) {
            allNums.push(i.toString());
      }
      assert.equal(pn.isConsistentNumberListPartioned(allNums), true);
    });
    // it('should return false when the argument is every number from 1000000 to 3000000', function(){
    //   var allNums = []
    //   for (var i = 1000000; i < 3000000; ++i) {
    //         allNums.push(i.toString());
    //   }
    //   assert.equal(pn.isConsistentNumberListTrie(allNums), true);
    // });
});

describe('insertPastLeaf', function() {
  it('', function(){
      assert.equal(pn.insertPastLeaf({}, "2"), true);
    });
  it('', function(){
      assert.equal(pn.insertPastLeaf({"2": {}}, "2"), false);
    });
  });

describe('insertAlreadyExists', function() {
  it('', function(){
      assert.equal(pn.insertAlreadyExists({"2": {"2": {}}}, "2", 1, 2), true);
    });
  it('', function(){
      assert.equal(pn.insertAlreadyExists({"2": {"2": {}}}, "2", 1, 3), false);
    });
  it('', function(){
      assert.equal(pn.insertAlreadyExists({"2": {"2": {}}}, "3", 1, 2), false);
    });
  });

describe('insertValid', function() {
  it('', function(){
      assert.equal(pn.insertValid({"2": {"2": {}}}, "2"), false);
    });
  it('', function(){
      assert.equal(pn.insertValid({"2": {"2": {}}}, "3"), true);
    });
  it('', function(){
      assert.equal(pn.insertValid({"2": {"2": {}}}, "222"), false);
    });
  it('', function(){
      assert.equal(pn.insertValid(
        {"2": {"2": {"3": {}}, "3": {"2": {}}}}, "33"), true);
    });
  it('', function(){
      assert.equal(pn.insertValid(
        {"2": {"2": {"3": {}}, "3": {"2": {}}}}, "224"), true);
    });
  it('', function(){
      assert.equal(pn.insertValid(
        {"2": {"2": {"3": {}}, "3": {"2": {}}}}, "23"), false);
    });
  it('', function(){
      assert.equal(pn.insertValid(
        {"2": {"2": {"3": {}}, "3": {"2": {}}}}, "223"), false);
    });
  it('', function(){
      assert.equal(pn.insertValid(
        {"2": {"2": {"3": {}}, "3": {"2": {}}}}, "2234"), false);
    });
  it('', function(){
      assert.equal(pn.insertValid(
        {}, "2"), false);
    });
  });

describe('isConsistentNumberListTrie', function() {
  it('', function(){
      assert.equal(pn.isConsistentNumberListTrie(["1", "2"]), true);
    });
  it('', function(){
      assert.equal(pn.isConsistentNumberListTrie(["1", "12"]), false);
    });
  it('', function(){
      assert.equal(pn.isConsistentNumberListTrie(["12", "1"]), false);
    });
  it('', function(){
      assert.equal(pn.isConsistentNumberListTrie(["12", "13"]), true);
    });
  });
