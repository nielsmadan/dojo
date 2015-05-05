var cluster = require('./cluster');
var assert = require("assert")

describe('cluster', function() {
    it('should return the empty list if it gets the empty list as an argument.', function(){
      assert.deepEqual(cluster.cluster([]), []);
    });
    it('', function(){
      assert.deepEqual(cluster.cluster([1, 2, 3, 4]), [[1, 2, 3, 4]]);
    });
    it('', function(){
      assert.deepEqual(cluster.cluster([1, 2, 3.9]), [[1, 2, 3.9]]);
    });
    it('it should seperate elements that are too far apart', function(){
      assert.deepEqual(cluster.cluster([1, 2, 4]), [[1, 2], 4]);
    });
    it('multiple numbers pull up the average', function(){
      assert.deepEqual(cluster.cluster([1, 2, 2, 4]), [[1, 2, 2, 4]]);
    });
    it('', function(){
      assert.deepEqual(cluster.cluster([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]]);
    });
    it('', function(){
      assert.deepEqual(cluster.cluster([1, 2, 10, 15, 16, 17, 20]), [[1, 2], 10, [15, 16, 17], 20]);
    });
});
