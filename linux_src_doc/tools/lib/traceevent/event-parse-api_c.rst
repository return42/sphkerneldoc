.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/lib/traceevent/event-parse-api.c

.. _`tep_get_first_event`:

tep_get_first_event
===================

.. c:function:: struct tep_event_format *tep_get_first_event(struct tep_handle *tep)

    returns the first event in the events array

    :param tep:
        a handle to the tep_handle
    :type tep: struct tep_handle \*

.. _`tep_get_first_event.description`:

Description
-----------

This returns pointer to the first element of the events array
If \ ``tep``\  is NULL, NULL is returned.

.. _`tep_get_events_count`:

tep_get_events_count
====================

.. c:function:: int tep_get_events_count(struct tep_handle *tep)

    get the number of defined events

    :param tep:
        a handle to the tep_handle
    :type tep: struct tep_handle \*

.. _`tep_get_events_count.description`:

Description
-----------

This returns number of elements in event array
If \ ``tep``\  is NULL, 0 is returned.

.. _`tep_set_flag`:

tep_set_flag
============

.. c:function:: void tep_set_flag(struct tep_handle *tep, int flag)

    set event parser flag

    :param tep:
        a handle to the tep_handle
    :type tep: struct tep_handle \*

    :param flag:
        flag, or combination of flags to be set
        can be any combination from enum tep_flag
    :type flag: int

.. _`tep_set_flag.description`:

Description
-----------

This sets a flag or mbination of flags  from enum tep_flag

.. _`tep_get_header_page_size`:

tep_get_header_page_size
========================

.. c:function:: int tep_get_header_page_size(struct tep_handle *pevent)

    get size of the header page

    :param pevent:
        a handle to the tep_handle
    :type pevent: struct tep_handle \*

.. _`tep_get_header_page_size.description`:

Description
-----------

This returns size of the header page
If \ ``pevent``\  is NULL, 0 is returned.

.. _`tep_get_cpus`:

tep_get_cpus
============

.. c:function:: int tep_get_cpus(struct tep_handle *pevent)

    get the number of CPUs

    :param pevent:
        a handle to the tep_handle
    :type pevent: struct tep_handle \*

.. _`tep_get_cpus.description`:

Description
-----------

This returns the number of CPUs
If \ ``pevent``\  is NULL, 0 is returned.

.. _`tep_set_cpus`:

tep_set_cpus
============

.. c:function:: void tep_set_cpus(struct tep_handle *pevent, int cpus)

    set the number of CPUs

    :param pevent:
        a handle to the tep_handle
    :type pevent: struct tep_handle \*

    :param cpus:
        *undescribed*
    :type cpus: int

.. _`tep_set_cpus.description`:

Description
-----------

This sets the number of CPUs

.. _`tep_get_long_size`:

tep_get_long_size
=================

.. c:function:: int tep_get_long_size(struct tep_handle *pevent)

    get the size of a long integer on the current machine

    :param pevent:
        a handle to the tep_handle
    :type pevent: struct tep_handle \*

.. _`tep_get_long_size.description`:

Description
-----------

This returns the size of a long integer on the current machine
If \ ``pevent``\  is NULL, 0 is returned.

.. _`tep_set_long_size`:

tep_set_long_size
=================

.. c:function:: void tep_set_long_size(struct tep_handle *pevent, int long_size)

    set the size of a long integer on the current machine

    :param pevent:
        a handle to the tep_handle
    :type pevent: struct tep_handle \*

    :param long_size:
        *undescribed*
    :type long_size: int

.. _`tep_set_long_size.description`:

Description
-----------

This sets the size of a long integer on the current machine

.. _`tep_get_page_size`:

tep_get_page_size
=================

.. c:function:: int tep_get_page_size(struct tep_handle *pevent)

    get the size of a memory page on the current machine

    :param pevent:
        a handle to the tep_handle
    :type pevent: struct tep_handle \*

.. _`tep_get_page_size.description`:

Description
-----------

This returns the size of a memory page on the current machine
If \ ``pevent``\  is NULL, 0 is returned.

.. _`tep_set_page_size`:

tep_set_page_size
=================

.. c:function:: void tep_set_page_size(struct tep_handle *pevent, int _page_size)

    set the size of a memory page on the current machine

    :param pevent:
        a handle to the tep_handle
    :type pevent: struct tep_handle \*

    :param _page_size:
        size of a memory page, in bytes
    :type _page_size: int

.. _`tep_set_page_size.description`:

Description
-----------

This sets the size of a memory page on the current machine

.. _`tep_is_file_bigendian`:

tep_is_file_bigendian
=====================

.. c:function:: int tep_is_file_bigendian(struct tep_handle *pevent)

    get if the file is in big endian order

    :param pevent:
        a handle to the tep_handle
    :type pevent: struct tep_handle \*

.. _`tep_is_file_bigendian.description`:

Description
-----------

This returns if the file is in big endian order
If \ ``pevent``\  is NULL, 0 is returned.

.. _`tep_set_file_bigendian`:

tep_set_file_bigendian
======================

.. c:function:: void tep_set_file_bigendian(struct tep_handle *pevent, enum tep_endian endian)

    set if the file is in big endian order

    :param pevent:
        a handle to the tep_handle
    :type pevent: struct tep_handle \*

    :param endian:
        non zero, if the file is in big endian order
    :type endian: enum tep_endian

.. _`tep_set_file_bigendian.description`:

Description
-----------

This sets if the file is in big endian order

.. _`tep_is_host_bigendian`:

tep_is_host_bigendian
=====================

.. c:function:: int tep_is_host_bigendian(struct tep_handle *pevent)

    get if the order of the current host is big endian

    :param pevent:
        a handle to the tep_handle
    :type pevent: struct tep_handle \*

.. _`tep_is_host_bigendian.description`:

Description
-----------

This gets if the order of the current host is big endian
If \ ``pevent``\  is NULL, 0 is returned.

.. _`tep_set_host_bigendian`:

tep_set_host_bigendian
======================

.. c:function:: void tep_set_host_bigendian(struct tep_handle *pevent, enum tep_endian endian)

    set the order of the local host

    :param pevent:
        a handle to the tep_handle
    :type pevent: struct tep_handle \*

    :param endian:
        non zero, if the local host has big endian order
    :type endian: enum tep_endian

.. _`tep_set_host_bigendian.description`:

Description
-----------

This sets the order of the local host

.. _`tep_is_latency_format`:

tep_is_latency_format
=====================

.. c:function:: int tep_is_latency_format(struct tep_handle *pevent)

    get if the latency output format is configured

    :param pevent:
        a handle to the tep_handle
    :type pevent: struct tep_handle \*

.. _`tep_is_latency_format.description`:

Description
-----------

This gets if the latency output format is configured
If \ ``pevent``\  is NULL, 0 is returned.

.. _`tep_set_latency_format`:

tep_set_latency_format
======================

.. c:function:: void tep_set_latency_format(struct tep_handle *pevent, int lat)

    set the latency output format

    :param pevent:
        a handle to the tep_handle
    :type pevent: struct tep_handle \*

    :param lat:
        non zero for latency output format
    :type lat: int

.. _`tep_set_latency_format.description`:

Description
-----------

This sets the latency output format

.. This file was automatic generated / don't edit.

