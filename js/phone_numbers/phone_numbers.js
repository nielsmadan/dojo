module.exports = {
    startsWith: function(target, prefix) {
        return _startsWith(target, prefix);
    },

    isValidPhoneNumber: function (phoneNumber) {
    	return _isValidPhoneNumber(phoneNumber);
    },

    isConsistentNumberList: function (validNumberList) {
    	return _isConsistentNumberList(validNumberList);
    },

    partitionList: function (validNumberList) {
    	return _partitionList(validNumberList);
    },

    getEmptyPartitionedList: function () {
    	return _getEmptyPartitionedList();
    },

    isConsistentNumberListPartioned: function (validNumberList) {
        return _isConsistentNumberListPartioned(validNumberList);
    },

    removeFirstDigit: function (partionedList){
        return _removeFirstDigit(partionedList);
    },

    partitionExhausted: function (partionedList) {
        return _partitionExhausted(partionedList);
    },

    insertPastLeaf: function (trie, number) {
        return _insertPastLeaf(trie, number);
    },

    insertAlreadyExists: function (trie, number, idx, length) {
        return _insertAlreadyExists(trie, number, idx, length)
    },

    insertValid: function (trie, number) {
        return _insertValid(trie, number);
    },

    isConsistentNumberListTrie: function (validNumberList) {
        return _isConsistentNumberListTrie(validNumberList);
    }
}

function _startsWith(target, prefix) {	
    if(target.substring(0, prefix.length) === prefix) {
    	return true;
    } else {
    	return false;
    }
}

function _getEmptyPartitionedList() {
	return [[], [], [], [], [], [], [], [], [], []];
}

function _partitionList(list) {
	var partionedList = _getEmptyPartitionedList();
    for (var i = 0; i < list.length; ++i) {
    	var index = list[i][0];
    	partionedList[index].push(list[i]);
    }

    return partionedList.filter(function (elem) { return elem.length != 0;});
}

function _isConsistentNumberList(validNumberList) {
	for(var i=0; i < validNumberList.length; ++i)
	{
		for (var j=i+1; j < validNumberList.length; ++j) {
			if (_startsWith(validNumberList[i], validNumberList[j]) ||
				_startsWith(validNumberList[j], validNumberList[i])) {
				return false;
			}
		}
	}
	
	return true;
}

function _isValidPhoneNumber(phoneNumber) {
	if (phoneNumber.match(/[A-Za-z]+/)) {
		return false;
	}
	if (phoneNumber.match(/\d+/)) {
		return true;
	}
}

// partition list
// remove first character
// if list contains one element = true
// if list contains two elements and one is "" = false

function _isConsistentNumberListPartioned(validNumberList) {
    return _isConsistentNumberListPartionedRecursive(_partitionList(validNumberList));
}

function _isConsistentNumberListPartionedRecursive(partionedList) {
    for (var i = 0; i < partionedList.length; ++i) {
        var newList = _removeFirstDigit(partionedList[i]);
        if (_partitionExhausted(newList)) {
            return false;
        } else {
            if (newList.length !== 1 &&
                _isConsistentNumberListPartionedRecursive(_partitionList(newList))
                === false) {
                return false;
            }
        }
    }

    return true;
}

function _removeFirstDigit(partionedList){
    return partionedList.map(function(element) { 
        return element.substring(1); 
    });    
}

function _partitionExhausted(partionedList) {
    return partionedList.length > 1 && partionedList.indexOf("") !== -1;
}

function _insertPastLeaf(curnode) {
    return Object.keys(curnode).length === 0;
}

function _insertAlreadyExists(curnode, number, idx, length) {
    return idx === length - 1 && curnode.hasOwnProperty(number);
}

//1. you insert past leaf
//2. you stop inserting on a place that already exists

function _insertValid(trie, number) {
    var curnode = trie;
    var ownBranch = false;
    for (var i = 0; i < number.length; ++i) {
        if (!ownBranch &&
            (_insertPastLeaf(curnode)
            || _insertAlreadyExists(curnode, number[i], i, number.length))) {
            return false;
        }
        if (curnode.hasOwnProperty(number[i])) {
            curnode = curnode[number[i]];
        } else {
            var newLetter = number[i];
            curnode[newLetter] = {};
            curnode = curnode[newLetter];
            ownBranch = true;
        }
    }

    return true;
}

function _isConsistentNumberListTrie (validNumberList) {
    var trie = {};

    var curnode = trie;
    for (var i = 0; i < validNumberList[0].length; ++i) {
        var newLetter = validNumberList[0][i];
        curnode[newLetter] = {};
        curnode = curnode[newLetter];
    }

    // initialize with first number
    for (var i = 1; i < validNumberList.length; ++i) {
        var res = _insertValid(trie, validNumberList[i]);
        if (res === false)
            return false;
    }
    return true;
}