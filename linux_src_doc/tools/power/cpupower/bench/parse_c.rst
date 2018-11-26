.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/power/cpupower/bench/parse.c

.. _`string_to_prio`:

string_to_prio
==============

.. c:function:: enum sched_prio string_to_prio(const char *str)

    :param str:
        *undescribed*
    :type str: const char \*

.. _`string_to_prio.description`:

Description
-----------

\ ``param``\  str string that represents a scheduler priority

\ ``retval``\  priority
\ ``retval``\  SCHED_ERR when the priority doesn't exit

.. _`prepare_output`:

prepare_output
==============

.. c:function:: FILE *prepare_output(const char *dirname)

    :param dirname:
        *undescribed*
    :type dirname: const char \*

.. _`prepare_output.description`:

Description
-----------

\ ``param``\  dir directory in which the logfile should be created

\ ``retval``\  logfile on success
\ ``retval``\  NULL when the file can't be created

.. _`prepare_default_config`:

prepare_default_config
======================

.. c:function:: struct config *prepare_default_config( void)

    :param void:
        no arguments
    :type void: 

.. _`prepare_default_config.description`:

Description
-----------

\ ``retval``\  default config on success
\ ``retval``\  NULL when the output file can't be created

.. _`prepare_config`:

prepare_config
==============

.. c:function:: int prepare_config(const char *path, struct config *config)

    :param path:
        *undescribed*
    :type path: const char \*

    :param config:
        *undescribed*
    :type config: struct config \*

.. _`prepare_config.description`:

Description
-----------

\ ``param``\  path config file name

\ ``retval``\  1 on error
\ ``retval``\  0 on success

.. This file was automatic generated / don't edit.

