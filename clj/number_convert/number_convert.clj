(ns number_convert)

(def number-map (hash-map 1 "one", 2 "two", 3 "three", 4 "four", 5 "five", 6 "six", 7 "seven", 8 "eight",
                          9 "nine", 10 "ten" 11 "eleven" 19 "nineteen"
                          20 "twenty", 30 "thirty", 90 "ninety"))

(declare number_to_string)

(defn int-div [input base]
  (int (/ input base)))

(defn subtract-mod [input base]
  (- input (mod input base)))

(defn get-multiple10-string [input]
  (get number-map (subtract-mod input 10)))

(defn get-lastdigit-string [input]
  (get number-map (mod input 10)))

(defn get-greater-19-string [input]
  (if (= (mod input 10) 0)
    (get number-map input)
    (str (get-multiple10-string input) "-" (get-lastdigit-string input))))

(defn get-less-than-19-string [input]
  (get number-map input))

(defn handle-tens [input]
  (let [input (mod input 100)]
    (if (> input 19)
      (get-greater-19-string input)
      (get-less-than-19-string input))))

(defn handle [input lower-bound upper-bound num-string fun]
  (let [input (mod input upper-bound)]
    (if (>= input lower-bound)
      (str (fun (int-div input lower-bound)) (str " " num-string)))))

(defn handle-hundreds [input]
  (handle input 100 1000 "hundred" #(get number-map %1)))

(defn handle-thousands [input]
  (handle input 1000 1000000 "thousand" number_to_string))

(defn handle-millions [input]
  (handle input 1000000 1000000000 "million" number_to_string))

(defn get-sep [input, sep, lower-bound, upper-bound]
  (let [input (mod input upper-bound)]
    (if (and (not= (mod input lower-bound) 0) (> input lower-bound))
         sep)))

(defn get-sep-millions [input]
  (get-sep input ", " 1000000 1000000000))

(defn get-sep-thousands [input]
  (get-sep input ", " 1000 1000000))

(defn get-sep-hundreds [input]
  (get-sep input " and " 100 1000))

(defn number_to_string [input]
  (str 
    (handle-millions input)
    (get-sep-millions input)
    (handle-thousands input)
    (get-sep-thousands input)
    (handle-hundreds input)
    (get-sep-hundreds input)
    (handle-tens input)))
