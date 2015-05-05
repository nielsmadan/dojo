module.exports = {
    cluster: function(seq) {
        return _cluster(seq);
    },
}

var CLUSTER_THRESHOLD = 2.5;

function average(seq) {
    return seq.reduce(function (a, b) { return a + b; }) / seq.length;
}

function _isInCluster(currentSeq, newElem) {
    return newElem - average(currentSeq) < CLUSTER_THRESHOLD;
}

function _getCluster(seq, pred) {
    var next = [seq[0]];

    for (var j = 1; j < seq.length && pred(next, seq[j]); ++j) {
        next.push(seq[j]);
    }

    return next;
}

function _cluster(seq) {
    if (seq.length === 0) {
        return [];
    }
    
    var result = [];

    var next = _getCluster(seq, _isInCluster);

    if (next.length > 1) {
        result.push(next);
    } else {
        result.push(next[0]);
    }

    return result + _cluster(seq.slice(next.length));
}
