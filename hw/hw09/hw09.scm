; (define-macro (list-of map-expr for var in lst if filter-expr)
;   `(if ,(null? lst) ())
;   `(if (lambda var (filter-expr var))
;   	(cons ,(lambda var (map-exp var)) (list-of map-exp for var in ,(cdr lst) if filter-expr))
;   	(list-of map-exp for var in ,(cdr lst) if filter-expr))
; )

(define-macro (check-null l)
	`(if ,(null? l) ()))

(define-macro (list-of map-expr for var in lst if filter-expr)
	`(map (lambda (,var) ,map-expr) (filter (lambda (,var) ,filter-expr) ,lst))
)