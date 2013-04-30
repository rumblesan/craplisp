
(define (double x) (* x 2))

(define (crazy x y z) (* x (+ y z)))

(double (crazy 4 5 (double 6 5)))

