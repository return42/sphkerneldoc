.. -*- coding: utf-8; mode: rst -*-

==============
c67x00-sched.c
==============


.. _`c67x00_ep_data`:

struct c67x00_ep_data
=====================

.. c:type:: c67x00_ep_data

    


.. _`c67x00_ep_data.definition`:

Definition
----------

.. code-block:: c

  struct c67x00_ep_data {
  };


.. _`c67x00_ep_data.members`:

Members
-------




.. _`c67x00_td`:

struct c67x00_td
================

.. c:type:: c67x00_td

    


.. _`c67x00_td.definition`:

Definition
----------

.. code-block:: c

  struct c67x00_td {
    #define TT_OFFSET		2
    #define TT_CONTROL		0
    #define TT_ISOCHRONOUS		1
    #define TT_BULK			2
    #define TT_INTERRUPT		3
  };


.. _`c67x00_td.members`:

Members
-------




.. _`c67x00_td.description`:

Description
-----------


Hardware parts are little endiannes, SW in CPU endianess.



.. _`dbg_td`:

dbg_td
======

.. c:function:: void dbg_td (struct c67x00_hcd *c67x00, struct c67x00_td *td, char *msg)

    Dump the contents of the TD

    :param struct c67x00_hcd \*c67x00:

        *undescribed*

    :param struct c67x00_td \*td:

        *undescribed*

    :param char \*msg:

        *undescribed*



.. _`frame_add`:

frame_add
=========

.. c:function:: u16 frame_add (u16 a, u16 b)

     Software wraparound for framenumbers.

    :param u16 a:

        *undescribed*

    :param u16 b:

        *undescribed*



.. _`frame_after`:

frame_after
===========

.. c:function:: int frame_after (u16 a, u16 b)

    is frame a after frame b

    :param u16 a:

        *undescribed*

    :param u16 b:

        *undescribed*



.. _`frame_after_eq`:

frame_after_eq
==============

.. c:function:: int frame_after_eq (u16 a, u16 b)

    is frame a after or equal to frame b

    :param u16 a:

        *undescribed*

    :param u16 b:

        *undescribed*



.. _`c67x00_release_urb`:

c67x00_release_urb
==================

.. c:function:: void c67x00_release_urb (struct c67x00_hcd *c67x00, struct urb *urb)

    remove link from all tds to this urb Disconnects the urb from it's tds, so that it can be given back.

    :param struct c67x00_hcd \*c67x00:

        *undescribed*

    :param struct urb \*urb:

        *undescribed*



.. _`c67x00_release_urb.pre`:

pre
---

urb->hcpriv != NULL



.. _`c67x00_create_td`:

c67x00_create_td
================

.. c:function:: int c67x00_create_td (struct c67x00_hcd *c67x00, struct urb *urb, void *data, int len, int pid, int toggle, unsigned long privdata)

    :param struct c67x00_hcd \*c67x00:

        *undescribed*

    :param struct urb \*urb:

        *undescribed*

    :param void \*data:

        *undescribed*

    :param int len:

        *undescribed*

    :param int pid:

        *undescribed*

    :param int toggle:

        *undescribed*

    :param unsigned long privdata:

        *undescribed*



.. _`c67x00_add_ctrl_urb`:

c67x00_add_ctrl_urb
===================

.. c:function:: int c67x00_add_ctrl_urb (struct c67x00_hcd *c67x00, struct urb *urb)

    :param struct c67x00_hcd \*c67x00:

        *undescribed*

    :param struct urb \*urb:

        *undescribed*



.. _`c67x00_parse_td`:

c67x00_parse_td
===============

.. c:function:: void c67x00_parse_td (struct c67x00_hcd *c67x00, struct c67x00_td *td)

    :param struct c67x00_hcd \*c67x00:

        *undescribed*

    :param struct c67x00_td \*td:

        *undescribed*



.. _`c67x00_check_td_list`:

c67x00_check_td_list
====================

.. c:function:: void c67x00_check_td_list (struct c67x00_hcd *c67x00)

    handle tds which have been processed by the c67x00

    :param struct c67x00_hcd \*c67x00:

        *undescribed*



.. _`c67x00_check_td_list.pre`:

pre
---

current_td == 0



.. _`c67x00_send_td`:

c67x00_send_td
==============

.. c:function:: void c67x00_send_td (struct c67x00_hcd *c67x00, struct c67x00_td *td)

    :param struct c67x00_hcd \*c67x00:

        *undescribed*

    :param struct c67x00_td \*td:

        *undescribed*



.. _`c67x00_do_work`:

c67x00_do_work
==============

.. c:function:: void c67x00_do_work (struct c67x00_hcd *c67x00)

    Schedulers state machine

    :param struct c67x00_hcd \*c67x00:

        *undescribed*

