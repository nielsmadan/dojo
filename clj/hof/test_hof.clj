(ns hof
  (:use clojure.test)
  (:use hof))

(deftest test-square
  (is (= (square 4) 16)))

(deftest test-fact
  (is (= (fact 5) 120)))

(deftest test-fact-new
  (is (= (fact-new 5) 120)))

(deftest test-fib
	(is (= (fib 7) 21)))

(deftest test-my-reduce-one
	(is (= (my-reduce + [1] 0) 1)))

(deftest test-my-reduce-multiple
	(is (= (my-reduce + [1 2 3] 0) 6)))

(deftest test-my-reduce-multiple
	(is (= (my-reduce + [1 2 3] 4) 10)))

(deftest test-my-map-one
	(is (= (my-map (fn [x] (* x x)) [3]) [9])))

(deftest test-my-map-multiple
	(is (= (my-map (fn [x] (* x x)) [1 3 5 7 9]) [1 9 25 49 81])))

(deftest test-my-filter-one
	(is (= (my-filter (fn [x] (= (mod x 2) 1)) []) [])))

(deftest test-my-and
	(is (= (my-and false (/ 1 0)) false)))

(deftest test-my-and-throws
	(try 
		(my-and true (/ 1 0))
		(is false)
	  (catch ArithmeticException e (is true))))

(deftest test-my-and
	(is (= (my-and false (/ 1 0)) false)))

(run-all-tests #"clojure.test.hof")
