.. -*- coding: utf-8; mode: rst -*-

=============
smartreflex.h
=============


.. _`sr_test_cond_timeout`:

sr_test_cond_timeout
====================

.. c:function:: sr_test_cond_timeout ( cond,  timeout,  index)

    busy-loop, testing a condition

    :param cond:
        condition to test until it evaluates to true

    :param timeout:
        maximum number of microseconds in the timeout

    :param index:
        loop index (integer)



.. _`sr_test_cond_timeout.description`:

Description
-----------

Loop waiting for ``cond`` to become true or until at least ``timeout``
microseconds have passed.  To use, define some integer ``index`` in the
calling code.  After running, if ``index`` == ``timeout``\ , then the loop has
timed out.



.. _`omap_sr_pmic_data`:

struct omap_sr_pmic_data
========================

.. c:type:: omap_sr_pmic_data

    Strucutre to be populated by pmic code to pass pmic specific info to smartreflex driver


.. _`omap_sr_pmic_data.definition`:

Definition
----------

.. code-block:: c

  struct omap_sr_pmic_data {
    void (* sr_pmic_init) (void);
  };


.. _`omap_sr_pmic_data.members`:

Members
-------

:``sr_pmic_init``:
    API to initialize smartreflex on the PMIC side.




.. _`omap_smartreflex_dev_attr`:

struct omap_smartreflex_dev_attr
================================

.. c:type:: omap_smartreflex_dev_attr

    Smartreflex Device attribute.


.. _`omap_smartreflex_dev_attr.definition`:

Definition
----------

.. code-block:: c

  struct omap_smartreflex_dev_attr {
    const char * sensor_voltdm_name;
  };


.. _`omap_smartreflex_dev_attr.members`:

Members
-------

:``sensor_voltdm_name``:
    Name of voltdomain of SR instance




.. _`omap_sr_class_data`:

struct omap_sr_class_data
=========================

.. c:type:: omap_sr_class_data

    Smartreflex class driver info


.. _`omap_sr_class_data.definition`:

Definition
----------

.. code-block:: c

  struct omap_sr_class_data {
    int (* enable) (struct omap_sr *sr);
    int (* disable) (struct omap_sr *sr, int is_volt_reset);
    int (* configure) (struct omap_sr *sr);
    int (* notify) (struct omap_sr *sr, u32 status);
    u8 notify_flags;
    u8 class_type;
  };


.. _`omap_sr_class_data.members`:

Members
-------

:``enable``:
    API to enable a particular class smaartreflex.

:``disable``:
    API to disable a particular class smartreflex.

:``configure``:
    API to configure a particular class smartreflex.

:``notify``:
    API to notify the class driver about an event in SR.
    Not needed for class3.

:``notify_flags``:
    specify the events to be notified to the class driver

:``class_type``:
    specify which smartreflex class.
    Can be used by the SR driver to take any class
    based decisions.




.. _`omap_sr_nvalue_table`:

struct omap_sr_nvalue_table
===========================

.. c:type:: omap_sr_nvalue_table

    Smartreflex n-target value info


.. _`omap_sr_nvalue_table.definition`:

Definition
----------

.. code-block:: c

  struct omap_sr_nvalue_table {
    u32 efuse_offs;
    u32 nvalue;
    u32 errminlimit;
    unsigned long volt_nominal;
  };


.. _`omap_sr_nvalue_table.members`:

Members
-------

:``efuse_offs``:
    The offset of the efuse where n-target values are stored.

:``nvalue``:
    The n-target value.

:``errminlimit``:
    The value of the ERRMINLIMIT bitfield for this n-target

:``volt_nominal``:
    microvolts DC that the VDD is initially programmed to




.. _`omap_sr_data`:

struct omap_sr_data
===================

.. c:type:: omap_sr_data

    Smartreflex platform data.


.. _`omap_sr_data.definition`:

Definition
----------

.. code-block:: c

  struct omap_sr_data {
    const char * name;
    int ip_type;
    u32 senp_mod;
    u32 senn_mod;
    int nvalue_count;
    bool enable_on_init;
    struct omap_sr_nvalue_table * nvalue_table;
    struct voltagedomain * voltdm;
  };


.. _`omap_sr_data.members`:

Members
-------

:``name``:
    instance name

:``ip_type``:
    Smartreflex IP type.

:``senp_mod``:
    SENPENABLE value of the sr CONFIG register

:``senn_mod``:
    SENNENABLE value for sr CONFIG register
    ``err_weight``                ERRWEIGHT value of the sr ERRCONFIG register
    ``err_maxlimit``        ERRMAXLIMIT value of the sr ERRCONFIG register
    ``accum_data``                ACCUMDATA value of the sr CONFIG register
    ``senn_avgweight``        SENNAVGWEIGHT value of the sr AVGWEIGHT register
    ``senp_avgweight``        SENPAVGWEIGHT value of the sr AVGWEIGHT register

:``nvalue_count``:
    Number of distinct nvalues in the nvalue table

:``enable_on_init``:
    whether this sr module needs to enabled at
    boot up or not.

:``nvalue_table``:
    table containing the  efuse offsets and nvalues
    corresponding to them.

:``voltdm``:
    Pointer to the voltage domain associated with the SR


