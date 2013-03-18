(ns clojure.test.number_convert
  (:use clojure.test)
  (:use number_convert))

(deftest test-one
  (is (= (number_to_string 1) "one")))

(deftest test-two
  (is (= (number_to_string 2) "two")))

(deftest test-three
  (is (= (number_to_string 3) "three")))

(deftest test-nineteen
  (is (= (number_to_string 19) "nineteen")))

(deftest test-twenty
  (is (= (number_to_string 20) "twenty")))

(deftest test-twenty-one
  (is (= (number_to_string 21) "twenty-one")))

(deftest test-ninety-nine
  (is (= (number_to_string 99) "ninety-nine")))

(deftest test-hundred
  (is (= (number_to_string 100) "one hundred")))

(deftest test-hundred-one
  (is (= (number_to_string 101) "one hundred and one")))

(deftest test-ninehundred-ninetynine
  (is (= (number_to_string 999) "nine hundred and ninety-nine")))

(deftest test-one-thousand
  (is (= (number_to_string 1000) "one thousand")))

(deftest test-one-thousand-one
  (is (= (number_to_string 1001) "one thousand, one")))

(deftest test-ten-thousand
  (is (= (number_to_string 10000) "ten thousand")))

(deftest test-hundred-thousand-one-thousand-one-hundred-eleven
  (is (= (number_to_string 101111) "one hundred and one thousand, one hundred and eleven")))

(deftest test-one-million
  (is (= (number_to_string 1000000) "one million")))

(deftest test-one-million-one-thousand
  (is (= (number_to_string 1001000) "one million, one thousand")))

(deftest test-one-million-one-thousand-and-one
  (is (= (number_to_string 1001001) "one million, one thousand, one")))

(deftest test-one-million-one-thousand-one-hundred-and-one
  (is (= (number_to_string 1001101) "one million, one thousand, one hundred and one")))

(deftest test-one-million-and-one
  (is (= (number_to_string 1000001) "one million, one")))

(deftest test-int-div-11
  (is (= (int-div 11 10) 1)))

(deftest test-int-div-160
  (is (= (int-div 160 100) 1)))

(deftest test-int-div-1000
  (is (= (int-div 1000 1000) 1)))

(deftest test-subtract-mod-25
  (is (= (subtract-mod 25 10) 20)))

(deftest test-get-multiple10-string
  (is (= (get-multiple10-string 21) "twenty")))

(deftest test-get-lastdigit-string
  (is (= (get-lastdigit-string 103) "three")))

(deftest test-get-less-than-19-string
  (is (= (get-less-than-19-string 19) "nineteen")))

(run-all-tests #"clojure.test.number_convert")
