.. -*- coding: utf-8; mode: rst -*-

=====
stm.h
=====

.. _`stp_policy_id`:

struct stp_policy_id
====================

.. c:type:: struct stp_policy_id

    identification for the STP policy



Definition
----------

.. code-block:: c

  struct stp_policy_id {
    __u32 size;
    __u16 master;
    __u16 channel;
    __u16 width;
    char id[0];
  };



Members
-------

:``size``:
    size of the structure including real id[] length

:``master``:
    assigned master

:``channel``:
    first assigned channel

:``width``:
    number of requested channels

:``id[0]``:
    identification string



Description
-----------

User must calculate the total size of the structure and put it into
``size`` field, fill out the ``id`` and desired ``width``\ . In return, kernel
fills out ``master``\ , ``channel`` and ``width``\ .

