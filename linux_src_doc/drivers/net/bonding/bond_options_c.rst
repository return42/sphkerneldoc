.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/bonding/bond_options.c

.. _`bond_opt_parse`:

bond_opt_parse
==============

.. c:function:: const struct bond_opt_value *bond_opt_parse(const struct bond_option *opt, struct bond_opt_value *val)

    parse option value

    :param opt:
        the option to parse against
    :type opt: const struct bond_option \*

    :param val:
        value to parse
    :type val: struct bond_opt_value \*

.. _`bond_opt_parse.description`:

Description
-----------

This function tries to extract the value from \ ``val``\  and check if it's
a possible match for the option and returns NULL if a match isn't found,
or the struct_opt_value that matched. It also strips the new line from
\ ``val->string``\  if it's present.

.. _`__bond_opt_set`:

\__bond_opt_set
===============

.. c:function:: int __bond_opt_set(struct bonding *bond, unsigned int option, struct bond_opt_value *val)

    set a bonding option

    :param bond:
        target bond device
    :type bond: struct bonding \*

    :param option:
        option to set
    :type option: unsigned int

    :param val:
        value to set it to
    :type val: struct bond_opt_value \*

.. _`__bond_opt_set.description`:

Description
-----------

This function is used to change the bond's option value, it can be
used for both enabling/changing an option and for disabling it. RTNL lock
must be obtained before calling this function.

.. _`__bond_opt_set_notify`:

\__bond_opt_set_notify
======================

.. c:function:: int __bond_opt_set_notify(struct bonding *bond, unsigned int option, struct bond_opt_value *val)

    set a bonding option

    :param bond:
        target bond device
    :type bond: struct bonding \*

    :param option:
        option to set
    :type option: unsigned int

    :param val:
        value to set it to
    :type val: struct bond_opt_value \*

.. _`__bond_opt_set_notify.description`:

Description
-----------

This function is used to change the bond's option value and trigger
a notification to user sapce. It can be used for both enabling/changing
an option and for disabling it. RTNL lock must be obtained before calling
this function.

.. _`bond_opt_tryset_rtnl`:

bond_opt_tryset_rtnl
====================

.. c:function:: int bond_opt_tryset_rtnl(struct bonding *bond, unsigned int option, char *buf)

    try to acquire rtnl and call \__bond_opt_set

    :param bond:
        target bond device
    :type bond: struct bonding \*

    :param option:
        option to set
    :type option: unsigned int

    :param buf:
        value to set it to
    :type buf: char \*

.. _`bond_opt_tryset_rtnl.description`:

Description
-----------

This function tries to acquire RTNL without blocking and if successful
calls \__bond_opt_set. It is mainly used for sysfs option manipulation.

.. _`bond_opt_get`:

bond_opt_get
============

.. c:function:: const struct bond_option *bond_opt_get(unsigned int option)

    get a pointer to an option

    :param option:
        option for which to return a pointer
    :type option: unsigned int

.. _`bond_opt_get.description`:

Description
-----------

This function checks if option is valid and if so returns a pointer
to its entry in the bond_opts[] option array.

.. This file was automatic generated / don't edit.

