.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/testing/selftests/kselftest_harness.h

.. _`example`:

example
=======

.. code-block:: c

    .. code-block:: c

       #include "../kselftest_harness.h"

       TEST(standalone_test) {
         do_some_stuff;
         EXPECT_GT(10, stuff) {
            stuff_state_t state;
            enumerate_stuff_state(&state);
            TH_LOG("expectation failed with state: %s", state.msg);
         }
         more_stuff;
         ASSERT_NE(some_stuff, NULL) TH_LOG("how did it happen?!");
         last_stuff;
         EXPECT_EQ(0, last_stuff);
       }

       FIXTURE(my_fixture) {
         mytype_t *data;
         int awesomeness_level;
       };
       FIXTURE_SETUP(my_fixture) {
         self->data = mytype_new();
         ASSERT_NE(NULL, self->data);
       }
       FIXTURE_TEARDOWN(my_fixture) {
         mytype_free(self->data);
       }
       TEST_F(my_fixture, data_is_good) {
         EXPECT_EQ(1, is_my_data_good(self->data));
       }

       TEST_HARNESS_MAIN


.. _`th_log`:

TH_LOG
======

.. c:function::  TH_LOG( fmt,  ...)

    :param fmt:
        format string
    :type fmt: 

    :param ellipsis ellipsis:
        optional arguments

.. _`th_log.description`:

Description
-----------

.. code-block:: c

    TH_LOG(format, ...)

Optional debug logging function available for use in tests.
Logging may be enabled or disabled by defining TH_LOG_ENABLED.
E.g., #define TH_LOG_ENABLED 1

If no definition is provided, logging is enabled by default.

If there is no way to print an error message for the process running the
test (e.g. not allowed to write to stderr), it is still possible to get the
ASSERT_* number for which the test failed.  This behavior can be enabled by
writing `_metadata->no_print = true;` before the check sequence that is
unable to print.  When an error occur, instead of printing an error message
and calling `abort(3)`, the test process call `_exit(2)` with the assert
number as argument, which is then printed by the parent process.

.. _`xfail`:

XFAIL
=====

.. c:function::  XFAIL( statement,  fmt,  ...)

    :param statement:
        statement to run after reporting XFAIL
    :type statement: 

    :param fmt:
        format string
    :type fmt: 

    :param ellipsis ellipsis:
        optional arguments

.. _`xfail.description`:

Description
-----------

This forces a "pass" after reporting a failure with an XFAIL prefix,
and runs "statement", which is usually "return" or "goto skip".

.. _`test`:

TEST
====

.. c:function::  TEST( test_name)

    Defines the test function and creates the registration stub

    :param test_name:
        test name
    :type test_name: 

.. _`test.description`:

Description
-----------

.. code-block:: c

    TEST(name) { implementation }

Defines a test by name.
Names must be unique and tests must not be run in parallel.  The
implementation containing block is a function and scoping should be treated
as such.  Returning early may be performed with a bare "return;" statement.

EXPECT_* and ASSERT_* are valid in a \ :c:func:`TEST`\  { } context.

.. _`test_signal`:

TEST_SIGNAL
===========

.. c:function::  TEST_SIGNAL( test_name,  signal)

    :param test_name:
        test name
    :type test_name: 

    :param signal:
        signal number
    :type signal: 

.. _`test_signal.description`:

Description
-----------

.. code-block:: c

    TEST_SIGNAL(name, signal) { implementation }

Defines a test by name and the expected term signal.
Names must be unique and tests must not be run in parallel.  The
implementation containing block is a function and scoping should be treated
as such.  Returning early may be performed with a bare "return;" statement.

EXPECT_* and ASSERT_* are valid in a \ :c:func:`TEST`\  { } context.

.. _`fixture_data`:

FIXTURE_DATA
============

.. c:function::  FIXTURE_DATA( datatype_name)

    Wraps the struct name so we have one less argument to pass around

    :param datatype_name:
        datatype name
    :type datatype_name: 

.. _`fixture_data.description`:

Description
-----------

.. code-block:: c

    FIXTURE_DATA(datatype name)

This call may be used when the type of the fixture data
is needed.  In general, this should not be needed unless
the *self* is being passed to a helper directly.

.. _`fixture`:

FIXTURE
=======

.. c:function::  FIXTURE( fixture_name)

    Called once per fixture to setup the data and register

    :param fixture_name:
        fixture name
    :type fixture_name: 

.. _`fixture.description`:

Description
-----------

.. code-block:: c

    FIXTURE(datatype name) {
      type property1;
      ...
    };

Defines the data provided to \ :c:func:`TEST_F`\ -defined tests as *self*.  It should be
populated and cleaned up using \ :c:func:`FIXTURE_SETUP`\  and \ :c:func:`FIXTURE_TEARDOWN`\ .

.. _`fixture_setup`:

FIXTURE_SETUP
=============

.. c:function::  FIXTURE_SETUP( fixture_name)

    Prepares the setup function for the fixture. *_metadata* is included so that EXPECT_* and ASSERT_* work correctly.

    :param fixture_name:
        fixture name
    :type fixture_name: 

.. _`fixture_setup.description`:

Description
-----------

.. code-block:: c

    FIXTURE_SETUP(fixture name) { implementation }

Populates the required "setup" function for a fixture.  An instance of the
datatype defined with \ :c:func:`FIXTURE_DATA`\  will be exposed as *self* for the
implementation.

ASSERT_* are valid for use in this context and will prempt the execution
of any dependent fixture tests.

A bare "return;" statement may be used to return early.

.. _`fixture_teardown`:

FIXTURE_TEARDOWN
================

.. c:function::  FIXTURE_TEARDOWN( fixture_name)

    *_metadata* is included so that EXPECT_* and ASSERT_* work correctly.

    :param fixture_name:
        fixture name
    :type fixture_name: 

.. _`fixture_teardown.description`:

Description
-----------

.. code-block:: c

    FIXTURE_TEARDOWN(fixture name) { implementation }

Populates the required "teardown" function for a fixture.  An instance of the
datatype defined with \ :c:func:`FIXTURE_DATA`\  will be exposed as *self* for the
implementation to clean up.

A bare "return;" statement may be used to return early.

.. _`test_f`:

TEST_F
======

.. c:function::  TEST_F( fixture_name,  test_name)

    Emits test registration and helpers for fixture-based test cases

    :param fixture_name:
        fixture name
    :type fixture_name: 

    :param test_name:
        test name
    :type test_name: 

.. _`test_f.description`:

Description
-----------

.. code-block:: c

    TEST_F(fixture, name) { implementation }

Defines a test that depends on a fixture (e.g., is part of a test case).
Very similar to \ :c:func:`TEST`\  except that *self* is the setup instance of fixture's
datatype exposed for use by the implementation.

Warning: use of ASSERT_* here will skip TEARDOWN.

.. _`test_harness_main`:

TEST_HARNESS_MAIN
=================

.. c:function::  TEST_HARNESS_MAIN()

    Simple wrapper to run the test harness

.. _`test_harness_main.description`:

Description
-----------

.. code-block:: c

    TEST_HARNESS_MAIN

Use once to append a \ :c:func:`main`\  to the test file.

.. _`operators`:

operators
=========

Operators for use in \ :c:func:`TEST`\  and \ :c:func:`TEST_F`\ .
ASSERT_* calls will stop test execution immediately.
EXPECT_* calls will emit a failure warning, note it, and continue.

.. _`assert_eq`:

ASSERT_EQ
=========

.. c:function::  ASSERT_EQ( expected,  seen)

    :param expected:
        expected value
    :type expected: 

    :param seen:
        measured value
    :type seen: 

.. _`assert_eq.description`:

Description
-----------

ASSERT_EQ(expected, measured): expected == measured

.. _`assert_ne`:

ASSERT_NE
=========

.. c:function::  ASSERT_NE( expected,  seen)

    :param expected:
        expected value
    :type expected: 

    :param seen:
        measured value
    :type seen: 

.. _`assert_ne.description`:

Description
-----------

ASSERT_NE(expected, measured): expected != measured

.. _`assert_lt`:

ASSERT_LT
=========

.. c:function::  ASSERT_LT( expected,  seen)

    :param expected:
        expected value
    :type expected: 

    :param seen:
        measured value
    :type seen: 

.. _`assert_lt.description`:

Description
-----------

ASSERT_LT(expected, measured): expected < measured

.. _`assert_le`:

ASSERT_LE
=========

.. c:function::  ASSERT_LE( expected,  seen)

    :param expected:
        expected value
    :type expected: 

    :param seen:
        measured value
    :type seen: 

.. _`assert_le.description`:

Description
-----------

ASSERT_LE(expected, measured): expected <= measured

.. _`assert_gt`:

ASSERT_GT
=========

.. c:function::  ASSERT_GT( expected,  seen)

    :param expected:
        expected value
    :type expected: 

    :param seen:
        measured value
    :type seen: 

.. _`assert_gt.description`:

Description
-----------

ASSERT_GT(expected, measured): expected > measured

.. _`assert_ge`:

ASSERT_GE
=========

.. c:function::  ASSERT_GE( expected,  seen)

    :param expected:
        expected value
    :type expected: 

    :param seen:
        measured value
    :type seen: 

.. _`assert_ge.description`:

Description
-----------

ASSERT_GE(expected, measured): expected >= measured

.. _`assert_null`:

ASSERT_NULL
===========

.. c:function::  ASSERT_NULL( seen)

    :param seen:
        measured value
    :type seen: 

.. _`assert_null.description`:

Description
-----------

ASSERT_NULL(measured): NULL == measured

.. _`assert_true`:

ASSERT_TRUE
===========

.. c:function::  ASSERT_TRUE( seen)

    :param seen:
        measured value
    :type seen: 

.. _`assert_true.description`:

Description
-----------

ASSERT_TRUE(measured): measured != 0

.. _`assert_false`:

ASSERT_FALSE
============

.. c:function::  ASSERT_FALSE( seen)

    :param seen:
        measured value
    :type seen: 

.. _`assert_false.description`:

Description
-----------

ASSERT_FALSE(measured): measured == 0

.. _`assert_streq`:

ASSERT_STREQ
============

.. c:function::  ASSERT_STREQ( expected,  seen)

    :param expected:
        expected value
    :type expected: 

    :param seen:
        measured value
    :type seen: 

.. _`assert_streq.description`:

Description
-----------

ASSERT_STREQ(expected, measured): !strcmp(expected, measured)

.. _`assert_strne`:

ASSERT_STRNE
============

.. c:function::  ASSERT_STRNE( expected,  seen)

    :param expected:
        expected value
    :type expected: 

    :param seen:
        measured value
    :type seen: 

.. _`assert_strne.description`:

Description
-----------

ASSERT_STRNE(expected, measured): strcmp(expected, measured)

.. _`expect_eq`:

EXPECT_EQ
=========

.. c:function::  EXPECT_EQ( expected,  seen)

    :param expected:
        expected value
    :type expected: 

    :param seen:
        measured value
    :type seen: 

.. _`expect_eq.description`:

Description
-----------

EXPECT_EQ(expected, measured): expected == measured

.. _`expect_ne`:

EXPECT_NE
=========

.. c:function::  EXPECT_NE( expected,  seen)

    :param expected:
        expected value
    :type expected: 

    :param seen:
        measured value
    :type seen: 

.. _`expect_ne.description`:

Description
-----------

EXPECT_NE(expected, measured): expected != measured

.. _`expect_lt`:

EXPECT_LT
=========

.. c:function::  EXPECT_LT( expected,  seen)

    :param expected:
        expected value
    :type expected: 

    :param seen:
        measured value
    :type seen: 

.. _`expect_lt.description`:

Description
-----------

EXPECT_LT(expected, measured): expected < measured

.. _`expect_le`:

EXPECT_LE
=========

.. c:function::  EXPECT_LE( expected,  seen)

    :param expected:
        expected value
    :type expected: 

    :param seen:
        measured value
    :type seen: 

.. _`expect_le.description`:

Description
-----------

EXPECT_LE(expected, measured): expected <= measured

.. _`expect_gt`:

EXPECT_GT
=========

.. c:function::  EXPECT_GT( expected,  seen)

    :param expected:
        expected value
    :type expected: 

    :param seen:
        measured value
    :type seen: 

.. _`expect_gt.description`:

Description
-----------

EXPECT_GT(expected, measured): expected > measured

.. _`expect_ge`:

EXPECT_GE
=========

.. c:function::  EXPECT_GE( expected,  seen)

    :param expected:
        expected value
    :type expected: 

    :param seen:
        measured value
    :type seen: 

.. _`expect_ge.description`:

Description
-----------

EXPECT_GE(expected, measured): expected >= measured

.. _`expect_null`:

EXPECT_NULL
===========

.. c:function::  EXPECT_NULL( seen)

    :param seen:
        measured value
    :type seen: 

.. _`expect_null.description`:

Description
-----------

EXPECT_NULL(measured): NULL == measured

.. _`expect_true`:

EXPECT_TRUE
===========

.. c:function::  EXPECT_TRUE( seen)

    :param seen:
        measured value
    :type seen: 

.. _`expect_true.description`:

Description
-----------

EXPECT_TRUE(measured): 0 != measured

.. _`expect_false`:

EXPECT_FALSE
============

.. c:function::  EXPECT_FALSE( seen)

    :param seen:
        measured value
    :type seen: 

.. _`expect_false.description`:

Description
-----------

EXPECT_FALSE(measured): 0 == measured

.. _`expect_streq`:

EXPECT_STREQ
============

.. c:function::  EXPECT_STREQ( expected,  seen)

    :param expected:
        expected value
    :type expected: 

    :param seen:
        measured value
    :type seen: 

.. _`expect_streq.description`:

Description
-----------

EXPECT_STREQ(expected, measured): !strcmp(expected, measured)

.. _`expect_strne`:

EXPECT_STRNE
============

.. c:function::  EXPECT_STRNE( expected,  seen)

    :param expected:
        expected value
    :type expected: 

    :param seen:
        measured value
    :type seen: 

.. _`expect_strne.description`:

Description
-----------

EXPECT_STRNE(expected, measured): strcmp(expected, measured)

.. This file was automatic generated / don't edit.

