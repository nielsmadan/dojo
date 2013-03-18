(ns game_of_life)


; Alive in next generation if: three neighbors || (alive && 2 neighbors)

(defn get-neighbors [[cell-x cell-y] & cell]
  (set (for [delta-x (range -1 2) delta-y (range -1 2)
             :when (not (and (= delta-x 0) (= delta-y 0)))]
          [(+ cell-x delta-x) (+ cell-y delta-y)])))

(defn count-alive-neighbors [cell alive-cell-list]
  (let [neighbors (get-neighbors cell)]
    (count
      (filter
        (fn [cell] (contains? alive-cell-list cell))
        neighbors))))

(defn is-currently-alive? [cell alive-cell-list]
  (contains? alive-cell-list cell))

(defn has-3-alive-neighbors? [cell alive-cell-list]
 	(= 3 (count-alive-neighbors cell alive-cell-list)))

(defn alive-and-2-neighbors? [cell alive-cell-list]
  (and (is-currently-alive? cell alive-cell-list)
  		(= 2 (count-alive-neighbors cell alive-cell-list))))

(defn alive-next-generation? [cell alive-cell-list]
  (or (has-3-alive-neighbors? cell alive-cell-list)
      (alive-and-2-neighbors? cell alive-cell-list)))

(defn get-candidates [cell-list]
  (set (mapcat get-neighbors cell-list)))

(defn get-next-generation [alive-cell-list]
  (set (filter (fn [e] (alive-next-generation? e alive-cell-list)) (get-candidates alive-cell-list))))

(defn get-printable-cell [cell alive-cell-list]
  (if (contains? alive-cell-list cell)
      "*" 
      "."))

(defn get-minmax-x-y [f cell-list]
  [(apply f (map (fn [e] (e 0)) cell-list))
   (apply f (map (fn [e] (e 1)) cell-list))])

(defn get-max-x-y [cell-list]
  (get-minmax-x-y max cell-list))

(defn get-min-x-y [cell-list]
  (get-minmax-x-y min cell-list))

(defn get-printable-line [cell-list start-cell length]
  (apply str (for [x (range (start-cell 0) (+ (start-cell 0) length))]
    (get-printable-cell [x (start-cell 1)] cell-list))))

(defn get-printable-grid [cell-list]
  (let [max-x-y (get-max-x-y cell-list)
        min-x-y (get-min-x-y cell-list)
        length (- (max-x-y 0) (min-x-y 0))]
    (clojure.string/join "\n" 
        (for [start-cell-y (range (max-x-y 1) (min-x-y 1))]
          (get-printable-line cell-list [(min-x-y 0) start-cell-y] length)))))

  ;; (set (for [delta-x (range -1 2) delta-y (range -1 2)
  ;;            :when (not (and (= delta-x 0) (= delta-y 0)))]
  ;;         [(+ cell-x delta-x) (+ cell-y delta-y)])))
