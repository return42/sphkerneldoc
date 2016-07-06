.. -*- coding: utf-8; mode: rst -*-

.. _races:

****************************
The Problem With Concurrency
****************************

(Skip this if you know what a Race Condition is).

In a normal program, you can increment a counter like so:


.. code-block:: c

          very_important_count++;

This is what they would expect to happen:



.. flat-table:: Expected Results
    :header-rows:  1
    :stub-columns: 0


    -  .. row 1

       -  Instance 1

       -  Instance 2

    -  .. row 2

       -  read very_important_count (5)

       -  

    -  .. row 3

       -  add 1 (6)

       -  

    -  .. row 4

       -  write very_important_count (6)

       -  

    -  .. row 5

       -  
       -  read very_important_count (6)

    -  .. row 6

       -  
       -  add 1 (7)

    -  .. row 7

       -  
       -  write very_important_count (7)


This is what might happen:



.. flat-table:: Possible Results
    :header-rows:  1
    :stub-columns: 0


    -  .. row 1

       -  Instance 1

       -  Instance 2

    -  .. row 2

       -  read very_important_count (5)

       -  

    -  .. row 3

       -  
       -  read very_important_count (5)

    -  .. row 4

       -  add 1 (6)

       -  

    -  .. row 5

       -  
       -  add 1 (6)

    -  .. row 6

       -  write very_important_count (6)

       -  

    -  .. row 7

       -  
       -  write very_important_count (6)



.. _race-condition:

Race Conditions and Critical Regions
====================================

This overlap, where the result depends on the relative timing of
multiple tasks, is called a race condition. The piece of code containing
the concurrency issue is called a critical region. And especially since
Linux starting running on SMP machines, they became one of the major
issues in kernel design and implementation.

Preemption can have the same effect, even if there is only one CPU: by
preempting one task during the critical region, we have exactly the same
race condition. In this case the thread which preempts might run the
critical region itself.

The solution is to recognize when these simultaneous accesses occur, and
use locks to make sure that only one instance can enter the critical
region at any time. There are many friendly primitives in the Linux
kernel to help you do this. And then there are the unfriendly
primitives, but I'll pretend they don't exist.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
