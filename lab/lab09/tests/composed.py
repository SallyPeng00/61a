test = {
  'name': 'composed',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> ((composed add-one add-one) 2)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> ((composed multiply-by-two multiply-by-two) 2)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> ((composed add-one multiply-by-two) 2)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> ((composed multiply-by-two add-one) 2)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> ((composed (composed add-one add-one) add-one) 2)
          a1bce68344d05cff1822ab9ad453b1cc
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> ((composed (composed add-one add-one) multiply-by-two) 2)
          5dd2f13fb4c4fd724ede9fca5662f722
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> ((composed multiply-by-two (composed add-one add-one)) 2)
          705c779aa26cefdacfc628f4e6fe0545
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'setup': r"""
      scm> (load 'lab09)
      scm> (load 'lab09_extra)
      scm> (define (add-one a) (+ a 1))
      scm> (define (multiply-by-two a) (* a 2))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
