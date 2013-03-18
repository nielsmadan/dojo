(ns clojure.test.game_of_life
  (:use clojure.test)
  (:use game_of_life))

(deftest test-get-neighbors-1-1
  (is (= (get-neighbors [1, 1]) #{[0, 0], [1, 0], [0, 1], [0, 2], [2, 0], [1, 2], [2, 1], [2, 2]})))

(deftest test-count-alive-neighbors-zero-neighbors
	( is (= (count-alive-neighbors [1, 1] #{}) 0 )))

(deftest test-count-alive-neighbors-one-neighbors
	( is (= (count-alive-neighbors [1, 1] #{[0, 0]}) 1 )))

(deftest test-count-alive-neighbors-two-neighbors
	( is (= (count-alive-neighbors [1, 1] #{[0, 0], [1, 0]}) 2 )))

(deftest test-count-alive-neighbors-two-neighbors-same-cell
	( is (= (count-alive-neighbors [1, 1] #{[0, 0], [1, 0], [1, 1]}) 2 )))

(deftest test-is-currently-alive
  (is (= (is-currently-alive? [1, 1] #{}) false)))

(deftest test-has-3-neighbors-false-less
  (is (= (has-3-alive-neighbors? [1 1] #{}) false)))

(deftest test-has-3-neighbors-false-more
  (is (= (has-3-alive-neighbors? [1 1] #{[0 0] [1 0] [ 0 1] [0 2] [2 0]}) false)))

(deftest test-has-3-neighbors-true
  (is (= (has-3-alive-neighbors? [1 1] #{[0 0] [1 0] [ 0 1]}) true)))

(deftest test-alive-and-two-neighbors-false-one-neighbors
  (is (= (alive-and-2-neighbors? [1 1] #{[0 1]}) false)))

(deftest test-alive-and-two-neighbors-false-one-neighbors-alive
  (is (= (alive-and-2-neighbors? [1 1] #{[0 1] [1 1]}) false)))

(deftest test-alive-and-two-neighbors-false-two-neighbors-not-alive
  (is (= (alive-and-2-neighbors? [1 1] #{[0 1] [1 0]}) false)))

(deftest test-alive-and-two-neighbors-true
  (is (= (alive-and-2-neighbors? [1 1] #{[1 1] [0 1] [1 0]}) true)))

(deftest test-alive-next-generation-two-neighbors-not-alive
  (is (= (alive-next-generation? [1 1] #{[0 0] [ 0 1]}) false)))

(deftest test-alive-next-generation-four-neighbors
  (is (= (alive-next-generation? [1 1] #{[0 0] [1 0] [0 1] [2 0]}) false)))

(deftest test-alive-next-generation-three-neighbors
  (is (= (alive-next-generation? [1 1] #{[0 0] [1 0] [0 1]}) true)))

(deftest test-alive-next-generation-three-neighbors-one-non-neighbor
  (is (= (alive-next-generation? [1 1] #{[0 0] [1 0] [0 1] [3 3]}) true)))

(deftest test-alive-next-generation-alive-two-neighbors
  (is (= (alive-next-generation? [1 1] #{[1 1] [1 0] [0 1]}) true)))

(deftest test-get-candidates
  (is (= (get-candidates #{[1 1]}) #{[0 0] [1 0] [0 1] [2 0] [0 2] [1 2] [2 1] [2 2]})))

(deftest test-get-next-generation-blinker
  (is (= (get-next-generation #{[0 1] [1 1] [2 1]}) #{[1 0] [1 1] [1 2]})))

(deftest test-get-next-generation-blinker-twice
  (is (= (get-next-generation (get-next-generation #{[0 1] [1 1] [2 1]})) #{[0 1] [1 1] [2 1]})))

(deftest test-get-printable-cell-alive
  (is (= (get-printable-cell [0 0] #{[1 0] [0 0]}) "*")))

(deftest test-get-printable-cell-dead
  (is (= (get-printable-cell [0 0] #{[1 0] [0 1]}) ".")))

(deftest test-get-max-x-y
  (is (= (get-max-x-y #{[0 0] [5 0] [0 5]}) [5 5])))

(deftest test-get-min-x-y
  (is (= (get-min-x-y #{[0 0] [-5 0] [0 -5]}) [-5 -5])))

(deftest test-get-printable-line
  (is (= (get-printable-line #{[0 1] [2 1]} [0 1] 3) "*.*")))

(deftest test-get-printable-grid
  (is (= (get-printable-grid #{[0 0] [1 1] [2 2]}) "..*\n.*.\n*..")))
;; (deftest test-print-blinker
;;   (is (= (get-printable-cells 

(run-all-tests #"clojure.test.game_of_life")
