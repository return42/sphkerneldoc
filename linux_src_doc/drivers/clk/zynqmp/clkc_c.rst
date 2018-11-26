.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/zynqmp/clkc.c

.. _`clock_parent`:

struct clock_parent
===================

.. c:type:: struct clock_parent

    Clock parent

.. _`clock_parent.definition`:

Definition
----------

.. code-block:: c

    struct clock_parent {
        char name[MAX_NAME_LEN];
        int id;
        u32 flag;
    }

.. _`clock_parent.members`:

Members
-------

name
    Parent name

id
    Parent clock ID

flag
    Parent flags

.. _`zynqmp_clock`:

struct zynqmp_clock
===================

.. c:type:: struct zynqmp_clock

    Clock

.. _`zynqmp_clock.definition`:

Definition
----------

.. code-block:: c

    struct zynqmp_clock {
        char clk_name[MAX_NAME_LEN];
        u32 valid;
        enum clk_type type;
        struct clock_topology node[MAX_NODES];
        u32 num_nodes;
        struct clock_parent parent[MAX_PARENT];
        u32 num_parents;
    }

.. _`zynqmp_clock.members`:

Members
-------

clk_name
    Clock name

valid
    Validity flag of clock

type
    Clock type (Output/External)

node
    Clock topology nodes

num_nodes
    Number of nodes present in topology

parent
    Parent of clock

num_parents
    Number of parents of clock

.. _`zynqmp_is_valid_clock`:

zynqmp_is_valid_clock
=====================

.. c:function:: int zynqmp_is_valid_clock(u32 clk_id)

    Check whether clock is valid or not

    :param clk_id:
        Clock index
    :type clk_id: u32

.. _`zynqmp_is_valid_clock.return`:

Return
------

1 if clock is valid, 0 if clock is invalid else error code

.. _`zynqmp_get_clock_name`:

zynqmp_get_clock_name
=====================

.. c:function:: int zynqmp_get_clock_name(u32 clk_id, char *clk_name)

    Get name of clock from Clock index

    :param clk_id:
        Clock index
    :type clk_id: u32

    :param clk_name:
        Name of clock
    :type clk_name: char \*

.. _`zynqmp_get_clock_name.return`:

Return
------

0 on success else error code

.. _`zynqmp_get_clock_type`:

zynqmp_get_clock_type
=====================

.. c:function:: int zynqmp_get_clock_type(u32 clk_id, u32 *type)

    Get type of clock

    :param clk_id:
        Clock index
    :type clk_id: u32

    :param type:
        Clock type: CLK_TYPE_OUTPUT or CLK_TYPE_EXTERNAL
    :type type: u32 \*

.. _`zynqmp_get_clock_type.return`:

Return
------

0 on success else error code

.. _`zynqmp_pm_clock_get_num_clocks`:

zynqmp_pm_clock_get_num_clocks
==============================

.. c:function:: int zynqmp_pm_clock_get_num_clocks(u32 *nclocks)

    Get number of clocks in system

    :param nclocks:
        Number of clocks in system/board.
    :type nclocks: u32 \*

.. _`zynqmp_pm_clock_get_num_clocks.description`:

Description
-----------

Call firmware API to get number of clocks.

.. _`zynqmp_pm_clock_get_num_clocks.return`:

Return
------

0 on success else error code.

.. _`zynqmp_pm_clock_get_name`:

zynqmp_pm_clock_get_name
========================

.. c:function:: int zynqmp_pm_clock_get_name(u32 clock_id, char *name)

    Get the name of clock for given id

    :param clock_id:
        ID of the clock to be queried
    :type clock_id: u32

    :param name:
        Name of given clock
    :type name: char \*

.. _`zynqmp_pm_clock_get_name.description`:

Description
-----------

This function is used to get name of clock specified by given
clock ID.

.. _`zynqmp_pm_clock_get_name.return`:

Return
------

Returns 0, in case of error name would be 0

.. _`zynqmp_pm_clock_get_topology`:

zynqmp_pm_clock_get_topology
============================

.. c:function:: int zynqmp_pm_clock_get_topology(u32 clock_id, u32 index, u32 *topology)

    Get the topology of clock for given id

    :param clock_id:
        ID of the clock to be queried
    :type clock_id: u32

    :param index:
        Node index of clock topology
    :type index: u32

    :param topology:
        Buffer to store nodes in topology and flags
    :type topology: u32 \*

.. _`zynqmp_pm_clock_get_topology.description`:

Description
-----------

This function is used to get topology information for the clock
specified by given clock ID.

This API will return 3 node of topology with a single response. To get
other nodes, master should call same API in loop with new
index till error is returned. E.g First call should have
index 0 which will return nodes 0,1 and 2. Next call, index
should be 3 which will return nodes 3,4 and 5 and so on.

.. _`zynqmp_pm_clock_get_topology.return`:

Return
------

0 on success else error+reason

.. _`zynqmp_clk_register_fixed_factor`:

zynqmp_clk_register_fixed_factor
================================

.. c:function:: struct clk_hw *zynqmp_clk_register_fixed_factor(const char *name, u32 clk_id, const char * const *parents, u8 num_parents, const struct clock_topology *nodes)

    Register fixed factor with the clock framework

    :param name:
        Name of this clock
    :type name: const char \*

    :param clk_id:
        Clock ID
    :type clk_id: u32

    :param parents:
        Name of this clock's parents
    :type parents: const char \* const \*

    :param num_parents:
        Number of parents
    :type num_parents: u8

    :param nodes:
        Clock topology node
    :type nodes: const struct clock_topology \*

.. _`zynqmp_clk_register_fixed_factor.return`:

Return
------

clock hardware to the registered clock

.. _`zynqmp_pm_clock_get_parents`:

zynqmp_pm_clock_get_parents
===========================

.. c:function:: int zynqmp_pm_clock_get_parents(u32 clock_id, u32 index, u32 *parents)

    Get the first 3 parents of clock for given id

    :param clock_id:
        Clock ID
    :type clock_id: u32

    :param index:
        Parent index
    :type index: u32

    :param parents:
        3 parents of the given clock
    :type parents: u32 \*

.. _`zynqmp_pm_clock_get_parents.description`:

Description
-----------

This function is used to get 3 parents for the clock specified by
given clock ID.

This API will return 3 parents with a single response. To get
other parents, master should call same API in loop with new
parent index till error is returned. E.g First call should have
index 0 which will return parents 0,1 and 2. Next call, index
should be 3 which will return parent 3,4 and 5 and so on.

.. _`zynqmp_pm_clock_get_parents.return`:

Return
------

0 on success else error+reason

.. _`zynqmp_pm_clock_get_attributes`:

zynqmp_pm_clock_get_attributes
==============================

.. c:function:: int zynqmp_pm_clock_get_attributes(u32 clock_id, u32 *attr)

    Get the attributes of clock for given id

    :param clock_id:
        Clock ID
    :type clock_id: u32

    :param attr:
        Clock attributes
    :type attr: u32 \*

.. _`zynqmp_pm_clock_get_attributes.description`:

Description
-----------

This function is used to get clock's attributes(e.g. valid, clock type, etc).

.. _`zynqmp_pm_clock_get_attributes.return`:

Return
------

0 on success else error+reason

.. _`__zynqmp_clock_get_topology`:

\__zynqmp_clock_get_topology
============================

.. c:function:: int __zynqmp_clock_get_topology(struct clock_topology *topology, u32 *data, u32 *nnodes)

    Get topology data of clock from firmware response data

    :param topology:
        Clock topology
    :type topology: struct clock_topology \*

    :param data:
        Clock topology data received from firmware
    :type data: u32 \*

    :param nnodes:
        Number of nodes
    :type nnodes: u32 \*

.. _`__zynqmp_clock_get_topology.return`:

Return
------

0 on success else error+reason

.. _`zynqmp_clock_get_topology`:

zynqmp_clock_get_topology
=========================

.. c:function:: int zynqmp_clock_get_topology(u32 clk_id, struct clock_topology *topology, u32 *num_nodes)

    Get topology of clock from firmware using PM_API

    :param clk_id:
        Clock index
    :type clk_id: u32

    :param topology:
        Clock topology
    :type topology: struct clock_topology \*

    :param num_nodes:
        Number of nodes
    :type num_nodes: u32 \*

.. _`zynqmp_clock_get_topology.return`:

Return
------

0 on success else error+reason

.. _`__zynqmp_clock_get_parents`:

\__zynqmp_clock_get_parents
===========================

.. c:function:: int __zynqmp_clock_get_parents(struct clock_parent *parents, u32 *data, u32 *nparent)

    Get parents info of clock from firmware response data

    :param parents:
        Clock parents
    :type parents: struct clock_parent \*

    :param data:
        Clock parents data received from firmware
    :type data: u32 \*

    :param nparent:
        Number of parent
    :type nparent: u32 \*

.. _`__zynqmp_clock_get_parents.return`:

Return
------

0 on success else error+reason

.. _`zynqmp_clock_get_parents`:

zynqmp_clock_get_parents
========================

.. c:function:: int zynqmp_clock_get_parents(u32 clk_id, struct clock_parent *parents, u32 *num_parents)

    Get parents info from firmware using PM_API

    :param clk_id:
        Clock index
    :type clk_id: u32

    :param parents:
        Clock parents
    :type parents: struct clock_parent \*

    :param num_parents:
        Total number of parents
    :type num_parents: u32 \*

.. _`zynqmp_clock_get_parents.return`:

Return
------

0 on success else error+reason

.. _`zynqmp_get_parent_list`:

zynqmp_get_parent_list
======================

.. c:function:: int zynqmp_get_parent_list(struct device_node *np, u32 clk_id, const char **parent_list, u32 *num_parents)

    Create list of parents name

    :param np:
        Device node
    :type np: struct device_node \*

    :param clk_id:
        Clock index
    :type clk_id: u32

    :param parent_list:
        List of parent's name
    :type parent_list: const char \*\*

    :param num_parents:
        Total number of parents
    :type num_parents: u32 \*

.. _`zynqmp_get_parent_list.return`:

Return
------

0 on success else error+reason

.. _`zynqmp_register_clk_topology`:

zynqmp_register_clk_topology
============================

.. c:function:: struct clk_hw *zynqmp_register_clk_topology(int clk_id, char *clk_name, int num_parents, const char **parent_names)

    Register clock topology

    :param clk_id:
        Clock index
    :type clk_id: int

    :param clk_name:
        Clock Name
    :type clk_name: char \*

    :param num_parents:
        Total number of parents
    :type num_parents: int

    :param parent_names:
        List of parents name
    :type parent_names: const char \*\*

.. _`zynqmp_register_clk_topology.return`:

Return
------

Returns either clock hardware or error+reason

.. _`zynqmp_register_clocks`:

zynqmp_register_clocks
======================

.. c:function:: int zynqmp_register_clocks(struct device_node *np)

    Register clocks

    :param np:
        Device node
    :type np: struct device_node \*

.. _`zynqmp_register_clocks.return`:

Return
------

0 on success else error code

.. _`zynqmp_get_clock_info`:

zynqmp_get_clock_info
=====================

.. c:function:: void zynqmp_get_clock_info( void)

    Get clock information from firmware using PM_API

    :param void:
        no arguments
    :type void: 

.. _`zynqmp_clk_setup`:

zynqmp_clk_setup
================

.. c:function:: int zynqmp_clk_setup(struct device_node *np)

    Setup the clock framework and register clocks

    :param np:
        Device node
    :type np: struct device_node \*

.. _`zynqmp_clk_setup.return`:

Return
------

0 on success else error code

.. This file was automatic generated / don't edit.

