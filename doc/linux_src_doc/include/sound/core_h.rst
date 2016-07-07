.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/sound/core.h

.. _`snd_printk`:

snd_printk
==========

.. c:function::  snd_printk( fmt,  args...)

    printk wrapper

    :param  fmt:
        format string

    :param  args...:
        variable arguments

.. _`snd_printk.description`:

Description
-----------

Works like \ :c:func:`printk`\  but prints the file and the line of the caller
when configured with CONFIG_SND_VERBOSE_PRINTK.

.. _`snd_printd`:

snd_printd
==========

.. c:function::  snd_printd( fmt,  args...)

    debug printk

    :param  fmt:
        format string

    :param  args...:
        variable arguments

.. _`snd_printd.description`:

Description
-----------

Works like \ :c:func:`snd_printk`\  for debugging purposes.
Ignored when CONFIG_SND_DEBUG is not set.

.. _`snd_bug`:

snd_BUG
=======

.. c:function::  snd_BUG( void)

    give a BUG warning message and stack trace

    :param  void:
        no arguments

.. _`snd_bug.description`:

Description
-----------

Calls \ :c:func:`WARN`\  if CONFIG_SND_DEBUG is set.
Ignored when CONFIG_SND_DEBUG is not set.

.. _`snd_printd_ratelimit`:

snd_printd_ratelimit
====================

.. c:function::  snd_printd_ratelimit( void)

    :param  void:
        no arguments

.. _`snd_bug_on`:

snd_BUG_ON
==========

.. c:function::  snd_BUG_ON( cond)

    debugging check macro

    :param  cond:
        condition to evaluate

.. _`snd_bug_on.description`:

Description
-----------

Has the same behavior as WARN_ON when CONFIG_SND_DEBUG is set,
otherwise just evaluates the conditional and returns the value.

.. _`snd_printdd`:

snd_printdd
===========

.. c:function::  snd_printdd( format,  args...)

    debug printk

    :param  format:
        format string

    :param  args...:
        variable arguments

.. _`snd_printdd.description`:

Description
-----------

Works like \ :c:func:`snd_printk`\  for debugging purposes.
Ignored when CONFIG_SND_DEBUG_VERBOSE is not set.

.. This file was automatic generated / don't edit.

