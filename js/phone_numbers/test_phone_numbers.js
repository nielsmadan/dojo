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
});
