(ns hof)


(defn square [x]
  (* x x))

(defn fact [n]
  (loop [cnt n acc 1]
    (if (zero? cnt)
      acc
      (recur (dec cnt) (* acc cnt)))))

(defn fact-new [n]
	(defn helper [cnt acc]
				    (if (zero? cnt)
      					acc
     					(helper (dec cnt) (* acc cnt))))
	(helper n 1))

(defn fib [n]
	(loop [x 0 y 1 cnt n]
		(if (zero? cnt)
			y
			(recur y ( + y x )(dec cnt)))))

(defn my-reduce [f lst start]
	(if (empty? lst)
		start
		(recur f (rest lst) (f start (first lst)))))

(defn my-map [f lst]
	(loop [res (vector) lft lst]
		(if (empty? lft)
			res
			(recur (conj res (f (first lft))) (rest lft)))))

(defn my-filter [f lst]
	(loop [res (vector) lft lst]
		(if (empty? lft)
			res
			(recur (if (f (first lft))
						(conj res (first lft))
						res)
			        (rest lft)))))

(defmacro my-and [cond1 cond2]
	`(if ~cond1
		~cond2
		false))