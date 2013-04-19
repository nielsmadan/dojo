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

    hasCommonPrefix: function (partionedList) {
        return _hasCommonPrefix(partionedList);
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
    return true;
}

function _removeFirstDigit(partionedList){
    return partionedList.map(function(element) { 
        return element.substring(1); 
    });    
}

function _hasCommonPrefix(partionedList) {
    return partionedList.length > 1 && partionedList.indexOf("") !== -1;
}