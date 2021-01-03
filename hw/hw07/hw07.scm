(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
	(car (cdr s))
)

(define (caddr s)
	(car (cdr (cdr s)))
)

(define (sign x)
	(cond
		((> x 0) 1)
		((= x 0) 0)
		(else -1))
)

(define (square x) (* x x))

(define (pow b n)
	(cond
		((= 1 n) b)
		((even? n) (pow (square b) (/ n 2)))
		(else (* (pow (square b) (floor (/ n 2))) b)))
)

(define (ordered? s)
	(cond
		((null? (cdr s)) #t)
		((> (car s) (car (cdr s))) #f)
		(else (ordered? (cdr s))))
)