
(define x 7)

(define y 10)

(define z 20)

(*
    (+ 1 2)
    (* 4 
        (cond (
               ((> x 7) x)
               ((= x 7) y)
               ((< x 7) z)
              ))
    )
)

