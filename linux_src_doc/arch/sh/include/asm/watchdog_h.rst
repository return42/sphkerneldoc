.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/sh/include/asm/watchdog.h

.. _`sh_wdt_read_cnt`:

sh_wdt_read_cnt
===============

.. c:function:: __u32 sh_wdt_read_cnt( void)

    Read from Counter Reads back the WTCNT value.

    :param  void:
        no arguments

.. _`sh_wdt_write_cnt`:

sh_wdt_write_cnt
================

.. c:function:: void sh_wdt_write_cnt(__u32 val)

    Write to Counter

    :param __u32 val:
        Value to write

.. _`sh_wdt_write_cnt.description`:

Description
-----------

Writes the given value \ ``val``\  to the lower byte of the timer counter.
The upper byte is set manually on each write.

.. _`sh_wdt_write_bst`:

sh_wdt_write_bst
================

.. c:function:: void sh_wdt_write_bst(__u32 val)

    Write to Counter

    :param __u32 val:
        Value to write

.. _`sh_wdt_write_bst.description`:

Description
-----------

Writes the given value \ ``val``\  to the lower byte of the timer counter.
The upper byte is set manually on each write.

.. _`sh_wdt_read_csr`:

sh_wdt_read_csr
===============

.. c:function:: __u32 sh_wdt_read_csr( void)

    Read from Control/Status Register

    :param  void:
        no arguments

.. _`sh_wdt_read_csr.description`:

Description
-----------

Reads back the WTCSR value.

.. _`sh_wdt_write_csr`:

sh_wdt_write_csr
================

.. c:function:: void sh_wdt_write_csr(__u32 val)

    Write to Control/Status Register

    :param __u32 val:
        Value to write

.. _`sh_wdt_write_csr.description`:

Description
-----------

Writes the given value \ ``val``\  to the lower byte of the control/status
register. The upper byte is set manually on each write.

.. _`sh_wdt_read_cnt`:

sh_wdt_read_cnt
===============

.. c:function:: __u8 sh_wdt_read_cnt( void)

    Read from Counter Reads back the WTCNT value.

    :param  void:
        no arguments

.. _`sh_wdt_write_cnt`:

sh_wdt_write_cnt
================

.. c:function:: void sh_wdt_write_cnt(__u8 val)

    Write to Counter

    :param __u8 val:
        Value to write

.. _`sh_wdt_write_cnt.description`:

Description
-----------

Writes the given value \ ``val``\  to the lower byte of the timer counter.
The upper byte is set manually on each write.

.. _`sh_wdt_read_csr`:

sh_wdt_read_csr
===============

.. c:function:: __u8 sh_wdt_read_csr( void)

    Read from Control/Status Register

    :param  void:
        no arguments

.. _`sh_wdt_read_csr.description`:

Description
-----------

Reads back the WTCSR value.

.. _`sh_wdt_write_csr`:

sh_wdt_write_csr
================

.. c:function:: void sh_wdt_write_csr(__u8 val)

    Write to Control/Status Register

    :param __u8 val:
        Value to write

.. _`sh_wdt_write_csr.description`:

Description
-----------

Writes the given value \ ``val``\  to the lower byte of the control/status
register. The upper byte is set manually on each write.

.. This file was automatic generated / don't edit.

