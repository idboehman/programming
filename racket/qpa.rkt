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
;; TODO: Rewrite total so semester-size can utilize it
;; total : num accessor list -> num
;; to compute the total of the accessor given of the given list
;; Examples: (total 0 class-qpa (semester-classes f11)) should return 51.665
(define (total sum arg lst)
  (cond [(empty? lst) sum]
        [else (total (+ (arg (first lst)) sum)
                     arg
                     (rest lst))]))
;; Tests:
(check-expect (total 0  class-qpa (semester-classes f11)) 51.665)
(check-expect (total 0 class-hrs (semester-classes f11)) 18)
(check-expect (total 0 s-total-qpa (year-semesters y1)) 110.335)

;; Contract, Purpose, Header:
;; semester-size : semester -> number
;; to compute the size of a semester, the number of classes taken
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
;; s-hours : semester -> number
;; to compute the number of credit hours in a semester 
;; Examples: (s-hours f11) should return 18
(define (s-hours s)
  (total 0 class-hrs (semester-classes s)))
;; Tests:
(check-expect (s-hours f11) 18)
(check-expect (s-hours sp12) 19)

;; Contract, Purpose, Header:
;; s-total-qpa : semester -> number
;; to compute the total qpa for the given semester
;; Examples: (s-total-qpa fall-11) should return 51.665
(define (s-total-qpa s)
  (total 0 class-qpa (semester-classes s)))
;; Tests:
(check-expect (s-total-qpa f11) 51.665)
(check-expect (s-total-qpa sp12) 58.67)

;; Contract, Purpose, Header:
;; s-qpa : [Listof class] -> number
;; to compute the qpa for the given semester
;; Examples: (s-qpa fall-11) should return 2.869
(define (s-qpa s)
  (/ (s-total-qpa s) (s-hours s)))
;; Tests:
(check-expect (s-qpa f11) (/ 51.665 18))
(check-expect (s-qpa sp12) (/ 58.67 19))

;; Contract, Purpose, Header:
;; y-total-qpa : year -> number
;; to compute the total qpa for a given year
;; Examples: (y-total-qpa y1) should return 107.668
(define (y-total-qpa y)
  (total 0 s-total-qpa (year-semesters y)))
;; Tests:
(check-expect (y-total-qpa y1) 110.335)

;; Contract, Purpose, Header:
;; y-hours : year -> number
;; to compute the total attempted credit hours for a given year
;; Examples: (y-hours y1) should return 37
(define (y-hours y)
  (total 0 s-hours (year-semesters y)))
;; Tests:
(check-expect (y-hours y1) 37)

;; Contract, Purpose, Header:
;; overall-qpa : year -> number
;; to compute the overall qpa for the list of semesters
;; Examples: (overall-qpa y1) should return 2.982
(define (overall-qpa y)
  (/ (y-total-qpa y) (y-hours y)))
;; Tests:
(check-expect (overall-qpa y1) (/ 110.335 37))

;; Contract, Purpose, Header:
;; qpa-needed : year number number -> number
;; to compute the qpa needed in the upcoming semester to obtain the given qpa
;; for the given number of credit hours (for the upcoming semester)
;; Examples: (qpa-needed y1 16 3) should return 3.0415625
(define (qpa-needed y hrs qpa)
  (local [(define future-total-hours (+ (y-hours y) hrs))
          (define future-total-qpa (* qpa future-total-hours))
          (define total-qpa-needed (- future-total-qpa (y-total-qpa y)))]
    (/ total-qpa-needed hrs)))
;; Tests:
(check-expect (qpa-needed y1 16 3) 3.0415625)

;; More tests

;; Fall 2012 classes
(define ood (make-class 3.667 4))
(define natd (make-class 4 4))
(define is2k (make-class 4 4))
(define stats (make-class 3.667 4))
;; Fall 2012 semester
(define f12 (make-semester (list ood natd is2k stats)))
;; Year 1.5
(define y1.5 (make-year (list f11 sp12 f12)))

;; Cumulative GPA for Semesters 1 - 3 = 3.239
(check-expect (overall-qpa y1.5) (/ 171.671 53))

;; What QPA do I need to earn Spring 2013 to maintain my current QPA?
(qpa-needed y1.5 16 (overall-qpa y1.5))
;; Need to get at least a 3.239 to maintain 3.239

;; What QPA do I need to earn Spring 2013 to get a 3.2?
(define three3 (qpa-needed y1.5 16 3.3))
;; Need to earn at least a 3.5 Spring 2013 to increase cumulative QPA 
;; to 3.3
(define three4 (qpa-needed y1.5 16 3.4))
;; Need to earn at least a 3.933 Spring 2013 to increase cumulative QPA
;; to 3.4

;; Speculation
;; Spring 2013 classes
(define hci (make-class 3 4)) ;; B
(define calc1 (make-class 2.333 4)) ;; C+
(define db (make-class 4 4)) ;; A
(define comporg (make-class 3.333 4)) ;; B+
;; Spring 2013 semester
(define sp13 (make-semester (list hci calc1 db comporg)))
;; Year 2
(define y2 (make-year (list f11 sp12 f12 sp13)))
;; Year 2 Cumulative GPA ~3.28
(define y2gpa (overall-qpa y2))

;; Spring 2014 classes
(define isdd (make-class 3 4))
(define empir (make-class 3 4))
(define systems (make-class 3.333 4))
(define cog (make-class 4 4))
;; Spring 2014 semester
(define sp14 (make-semester (list isdd empir systems cog)))
;; Year 2.667
(define y2.6 (make-year (list f11 sp12 f12 sp13 sp14)))
;; Year 2.667 Cumulative GPA ~3.29
(define y2.6gpa (overall-qpa y2.6))

;; Summer 1 2014 classes
(define advw (make-class 3.667 4))
(define anth (make-class 4 4))
;; Half Semester 1: Summer 1 2014
(define sum14 (make-semester (list advw anth)))
;; Year 3
(define y3 (make-year (list f11 sp12 f12 sp13 sp14 sum14)))
;; Year 3 Cumulative GPA ~3.336
(define y3gpa (overall-qpa y3))

  

