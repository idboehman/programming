;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname qpa) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ())))
;; Program for different QPA Calculations 
;; Based on: http://www.northeastern.edu/registrar/gradecalc.html

;; Data Analysis & Definitions:
(define-struct class (grade hrs))
;; A class is a structure: (make-class g h) where g and h are numbers
;; and g is defined to three decimal places as used by NEU grades

(define-struct semester (classes))
;; A semester is a structure: (make-semester c) where c is a [Listof class]

(define-struct year (semesters))
;; A year is a structure: (make-year s) where s is a [Listof semester]

;; Class examples
;; Fall 2011 classes
(define film (make-class 3.000 4))
(define overview (make-class 4.000 1))
(define discrete (make-class 2.667 4))
(define fundies (make-class 2.333 4))
(define fundies-lab (make-class 2.333 1))
(define english (make-class 3.333 4))
;; Spring 2012 classes
(define overview2 (make-class 4.000 1))
(define logic (make-class 2.667 4))
(define logic-lab (make-class 2.667 1))
(define fundies2 (make-class 2.667 4))
(define fundies2-lab (make-class 2.667 1))
(define psych (make-class 4.000 4))
(define micro (make-class 3.000 4))

;; Semester examples
;; Fall 2011 semester
(define f11 (make-semester (list film overview
                                 discrete fundies
                                 fundies-lab english)))
;; Spring 2012 semester
(define sp12 (make-semester (list overview2 logic
                                  logic-lab fundies2
                                  fundies2-lab psych
                                  micro)))

;; Year examples
;; Year 1
(define y1 (make-year (list f11 sp12)))

;; Function declarations

;; Contract, Purpose, Header:
;; class-qpa : class -> number
;; to compute the QPA earned for a class
;; Examples: (class-qpa (make-class 4 1)) should return 4
(define (class-qpa class)
  (* (class-grade class) (class-hrs class)))

;; Tests:
(check-expect (class-qpa overview) 4)
(check-expect (class-qpa micro) 12)
(check-expect (class-qpa fundies2) 10.668)

;; Contract, Purpose, Header:
;; semester-size : semester -> number
;; to compute the size of a semester
;; Examples: (semester-size f11) should return 6
(define (semester-size s)
  (local [(define (size sum loc)
            (cond [(empty? loc) sum]
                  [else (size (+ 1 sum) (rest loc))]))]
    (size 0 (semester-classes s))))

;; Tests:
(check-expect (semester-size f11) 6)
(check-expect (semester-size sp12) 7)

;; Contract, Purpose, Header:
;; semester-hours : semester -> number
;; to compute the number of credit hours in a semester 
;; Examples: (semester-hours f11) should return 18
(define (semester-hours s)
  (local [(define (hours sum loc)
            (cond [(empty? loc) sum]
                  [else (hours (+ (class-hrs (first loc)) sum)
                               (rest loc))]))]
    (hours 0 (semester-classes s))))

;; Tests:
(check-expect (semester-hours f11) 18)
(check-expect (semester-hours sp12) 19)

;; Contract, Purpose, Header:
;; semester-total-qpa : semester -> number
;; to compute the total qpa for the given semester
;; Examples: (semester-total-qpa fall-11) should return 51.665
(define (semester-total-qpa s)
  (local [(define (total-qpa sum loc)
            (cond [(empty? loc) sum]
                  [else (total-qpa (+ (class-qpa (first loc))
                                      sum)
                                   (rest loc))]))]
    (total-qpa 0 (semester-classes s))))

;; Tests:
(check-expect (semester-total-qpa f11) 51.665)
(check-expect (semester-total-qpa sp12) 58.67)

;; Contract, Purpose, Header:
;; semester-qpa : [Listof class] -> number
;; to compute the qpa for the given semester
;; Examples: (semester-qpa fall-11) should return 2.869
(define (semester-qpa s)
  (/ (semester-total-qpa s) (semester-hours s)))

;; Tests:
(check-expect (semester-qpa f11) (/ 51.665 18))
(check-expect (semester-qpa sp12) (/ 58.67 19))

;; Contract, Purpose, Header:
;; total-year-qpa : year -> number
;; to compute the total qpa for a given year
;; Examples: (total-year-qpa y1) should return 107.668
(define (total-year-qpa y)
  (local [(define (year-qpa sum los)
            (cond [(empty? los) sum]
                  [else (year-qpa (+ (semester-total-qpa (first los)) sum)
                                  (rest los))]))]
  (year-qpa 0 (year-semesters y))))

;; Tests:
(check-expect (total-year-qpa y1) 110.335)

;; Contract, Purpose, Header:
;; total-hours : year -> number
;; to compute the total attempted credit hours for a given year
;; Examples: (total-hours y1) should return 37
(define (total-hours y)
  (local [(define (hours sum los)
            (cond [(empty? los) sum]
                  [else (hours (+ (semester-hours (first los)) sum)
                               (rest los))]))]
    (hours 0 (year-semesters y))))

;; Tests:
(check-expect (total-hours y1) 37)

;; Contract, Purpose, Header:
;; overall-qpa : year -> number
;; to compute the overall qpa for the list of semesters
;; Examples: (overall-qpa y1) should return 2.982
(define (overall-qpa y)
  (/ (total-year-qpa y) (total-hours y)))

;; Tests:
(check-expect (overall-qpa y1) (/ 110.335 37))

;; Contract, Purpose, Header:
;; qpa-needed : year number number -> number
;; to compute the qpa needed in the upcoming semester to obtain the given qpa
;; for the given number of credit hours (for the upcoming semester)
;; Examples: (qpa-needed y1) should return 3.0415625
(define (qpa-needed y hrs qpa)
  (local [(define future-total-hours (+ (total-hours y) hrs))
          (define future-total-qpa (* qpa future-total-hours))
          (define total-qpa-needed (- future-total-qpa (total-year-qpa y)))]
    (/ total-qpa-needed hrs)))

;; Tests:
(check-expect (qpa-needed y1 16 3) 3.0415625)

;; More tests

;; Fall 2012 classes
(define ood (make-class 3.667 4))
(define natd (make-class 4 4))
(define is2k (make-class 2.667 4)) ;; Getting a B- at lowest
(define stats (make-class 3.667 4))
;; Fall 2012 semester
(define f12 (make-semester (list ood natd is2k stats)))
;; Year 1.5
(define y1.5 (make-year (list f11 sp12 f12)))
;; Predicted QPA for year 1.5 (IS2K grade not finalized yet)
(overall-qpa y1.5)
;; What QPA do I need to earn Spring 2013 to maintain my current QPA?
(qpa-needed y1.5 16 (overall-qpa y1.5)) ;; 3.139
;; What QPA do I need to earn Spring 2013 to get a 3.2?
(qpa-needed y1.5 16 3.2) ;; 3.404


