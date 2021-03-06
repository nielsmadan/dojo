module.exports = {
    zero: _zero,
    increment: function (church_num) {
        return _increment(church_num);
    },
    unwind: function (church_num, fn) {
        return _unwind(church_num, fn);
    },
    add: function (num1, num2) {
        return _add(num1, num2);
    },
    mul: function (num1, num2) {
        return _mul(num1, num2);
    }
}


function _zero(fn) {
    return function (x) {
        return x;
    }
}


function _one(fn) {
    return function (x) {
        return fn(x);
    }
}


function _succ(church_num) {
    return function (fn) {
        return function (x) {
            return fn(church_num(fn)(x));
        }
    }
}

function _two(fn) {
    return function (x) {
        return fn(fn(x));
    }
}


function _three(fn) {
    return function (x) {
        return fn(fn(fn(x)));
    }
}


function _increment(church_num) {
    return function (fn) {
        return function (value) {
            return fn(church_num(fn)(value));
        }
    }
}


function _unwind(church_num, fn) { 
    var result = church_num(fn);
    while (result !== fn) {
        result = result(fn);
    }
}


function _add(num1, num2) {
    return function (fn) {
        return function (value) {
            return num1(fn)(num2(fn)(value));
        }
    }
}

function _mul(num1, num2) {
    return function (fn) {
        return num1(num2(fn));
    }
}


/* mult ≡ λm.λn.λf. m (n f) */

// (define (add-church m n)
//    (lambda (f) (lambda (x) ((m f) ((n f) x)))))
// function _increment(zero) {
//     return function (printBar) {
//         return function (null) {
//             return printBar(zero(printBar)(null));
//         }
//     }
// }
// (define (add-1 n)
//     (lambda (f) (lambda (x) (f ((n f) x)))))
