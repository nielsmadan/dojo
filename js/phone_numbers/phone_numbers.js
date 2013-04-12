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


var numList = ["1", "2", "3", "4", "5", "6", "7", "8", "9"];

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

