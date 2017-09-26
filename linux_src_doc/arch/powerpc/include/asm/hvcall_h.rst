.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/include/asm/hvcall.h

.. _`plpar_hcall_norets`:

plpar_hcall_norets
==================

.. c:function:: long plpar_hcall_norets(unsigned long opcode,  ...)

    - Make a pseries hypervisor call with no return arguments

    :param unsigned long opcode:
        The hypervisor call to make.

    :param ellipsis ellipsis:
        variable arguments

.. _`plpar_hcall_norets.description`:

Description
-----------

This call supports up to 7 arguments and only returns the status of
the hcall. Use this version where possible, its slightly faster than
the other plpar_hcalls.

.. _`plpar_hcall_bufsize`:

PLPAR_HCALL_BUFSIZE
===================

.. c:function::  PLPAR_HCALL_BUFSIZE()

    - Make a pseries hypervisor call

.. _`plpar_hcall_bufsize.description`:

Description
-----------

This call supports up to 6 arguments and 4 return arguments. Use
PLPAR_HCALL_BUFSIZE to size the return argument buffer.

Used for all but the craziest of phyp interfaces (see plpar_hcall9)

.. _`plpar_hcall_raw`:

plpar_hcall_raw
===============

.. c:function:: long plpar_hcall_raw(unsigned long opcode, unsigned long *retbuf,  ...)

    - Make a hypervisor call without calculating hcall stats

    :param unsigned long opcode:
        The hypervisor call to make.

    :param unsigned long \*retbuf:
        Buffer to store up to 4 return arguments in.

    :param ellipsis ellipsis:
        variable arguments

.. _`plpar_hcall_raw.description`:

Description
-----------

This call supports up to 6 arguments and 4 return arguments. Use
PLPAR_HCALL_BUFSIZE to size the return argument buffer.

Used when phyp interface needs to be called in real mode. Similar to
plpar_hcall, but plpar_hcall_raw works in real mode and does not
calculate hypervisor call statistics.

.. _`plpar_hcall9_bufsize`:

PLPAR_HCALL9_BUFSIZE
====================

.. c:function::  PLPAR_HCALL9_BUFSIZE()

    - Make a pseries hypervisor call with up to 9 return arguments

.. _`plpar_hcall9_bufsize.description`:

Description
-----------

This call supports up to 9 arguments and 9 return arguments. Use
PLPAR_HCALL9_BUFSIZE to size the return argument buffer.

.. This file was automatic generated / don't edit.

