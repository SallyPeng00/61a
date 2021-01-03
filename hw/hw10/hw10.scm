(define (accumulate combiner start n term)
  (define (range a c)
  	(cond
  		((= a c) (list a))
  		(else (cons c (range a (+ c 1))))))
  (define lst (range n 1))
  (combiner start (reduce combiner (map (lambda (x) (term x)) lst)))
)

(define (accumulate-tail combiner start n term)
	(cond
	((= n 0) start)
	(else (accumulate-tail combiner (combiner start (term n)) (- n 1) term)))

)

(define (rle s)
	(define (helper prev count s)
		(cond
			((null? s) (cons-stream (list prev count) nil))
			((eq? (car s) prev) (helper prev (+ count 1) (cdr-stream s)))
			(else (cons-stream (list prev count) (helper (car s) 1 (cdr-stream s))))))

  
  (cond
  	((null? s) '())
  	(else (helper (car s) 1 (cdr-stream s))))
)