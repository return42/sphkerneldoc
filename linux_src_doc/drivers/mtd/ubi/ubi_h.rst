.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/ubi/ubi.h

.. _`ubi_vid_io_buf`:

struct ubi_vid_io_buf
=====================

.. c:type:: struct ubi_vid_io_buf

    VID buffer used to read/write VID info to/from the flash.

.. _`ubi_vid_io_buf.definition`:

Definition
----------

.. code-block:: c

    struct ubi_vid_io_buf {
        struct ubi_vid_hdr *hdr;
        void *buffer;
    }

.. _`ubi_vid_io_buf.members`:

Members
-------

hdr
    a pointer to the VID header stored in buffer

buffer
    underlying buffer

.. _`ubi_wl_entry`:

struct ubi_wl_entry
===================

.. c:type:: struct ubi_wl_entry

    wear-leveling entry.

.. _`ubi_wl_entry.definition`:

Definition
----------

.. code-block:: c

    struct ubi_wl_entry {
        union {
            struct rb_node rb;
            struct list_head list;
        } u;
        int ec;
        int pnum;
    }

.. _`ubi_wl_entry.members`:

Members
-------

u
    *undescribed*

u.rb
    link in the corresponding (free/used) RB-tree

u.list
    link in the protection queue

ec
    erase counter

pnum
    physical eraseblock number

.. _`ubi_wl_entry.description`:

Description
-----------

This data structure is used in the WL sub-system. Each physical eraseblock
has a corresponding \ :c:type:`struct wl_entry <wl_entry>`\  object which may be kept in different
RB-trees. See WL sub-system for details.

.. _`ubi_ltree_entry`:

struct ubi_ltree_entry
======================

.. c:type:: struct ubi_ltree_entry

    an entry in the lock tree.

.. _`ubi_ltree_entry.definition`:

Definition
----------

.. code-block:: c

    struct ubi_ltree_entry {
        struct rb_node rb;
        int vol_id;
        int lnum;
        int users;
        struct rw_semaphore mutex;
    }

.. _`ubi_ltree_entry.members`:

Members
-------

rb
    links RB-tree nodes

vol_id
    volume ID of the locked logical eraseblock

lnum
    locked logical eraseblock number

users
    how many tasks are using this logical eraseblock or wait for it

mutex
    read/write mutex to implement read/write access serialization to
    the (@vol_id, \ ``lnum``\ ) logical eraseblock

.. _`ubi_ltree_entry.description`:

Description
-----------

This data structure is used in the EBA sub-system to implement per-LEB
locking. When a logical eraseblock is being locked - corresponding
\ :c:type:`struct ubi_ltree_entry <ubi_ltree_entry>`\  object is inserted to the lock tree (@ubi->ltree).
See EBA sub-system for details.

.. _`ubi_rename_entry`:

struct ubi_rename_entry
=======================

.. c:type:: struct ubi_rename_entry

    volume re-name description data structure.

.. _`ubi_rename_entry.definition`:

Definition
----------

.. code-block:: c

    struct ubi_rename_entry {
        int new_name_len;
        char new_name[UBI_VOL_NAME_MAX + 1];
        int remove;
        struct ubi_volume_desc *desc;
        struct list_head list;
    }

.. _`ubi_rename_entry.members`:

Members
-------

new_name_len
    new volume name length

new_name
    new volume name

remove
    if not zero, this volume should be removed, not re-named

desc
    descriptor of the volume

list
    links re-name entries into a list

.. _`ubi_rename_entry.description`:

Description
-----------

This data structure is utilized in the multiple volume re-name code. Namely,
UBI first creates a list of \ :c:type:`struct ubi_rename_entry <ubi_rename_entry>`\  objects from the
\ :c:type:`struct ubi_rnvol_req <ubi_rnvol_req>`\  request object, and then utilizes this list to do all
the job.

.. _`ubi_fastmap_layout`:

struct ubi_fastmap_layout
=========================

.. c:type:: struct ubi_fastmap_layout

    in-memory fastmap data structure.

.. _`ubi_fastmap_layout.definition`:

Definition
----------

.. code-block:: c

    struct ubi_fastmap_layout {
        struct ubi_wl_entry *e[UBI_FM_MAX_BLOCKS];
        int to_be_tortured[UBI_FM_MAX_BLOCKS];
        int used_blocks;
        int max_pool_size;
        int max_wl_pool_size;
    }

.. _`ubi_fastmap_layout.members`:

Members
-------

e
    PEBs used by the current fastmap

to_be_tortured
    if non-zero tortured this PEB

used_blocks
    number of used PEBs

max_pool_size
    maximal size of the user pool

max_wl_pool_size
    maximal size of the pool used by the WL sub-system

.. _`ubi_fm_pool`:

struct ubi_fm_pool
==================

.. c:type:: struct ubi_fm_pool

    in-memory fastmap pool

.. _`ubi_fm_pool.definition`:

Definition
----------

.. code-block:: c

    struct ubi_fm_pool {
        int pebs[UBI_FM_MAX_POOL_SIZE];
        int used;
        int size;
        int max_size;
    }

.. _`ubi_fm_pool.members`:

Members
-------

pebs
    PEBs in this pool

used
    number of used PEBs

size
    total number of PEBs in this pool

max_size
    maximal size of the pool

.. _`ubi_fm_pool.description`:

Description
-----------

A pool gets filled with up to max_size.
If all PEBs within the pool are used a new fastmap will be written
to the flash and the pool gets refilled with empty PEBs.

.. _`ubi_eba_leb_desc`:

struct ubi_eba_leb_desc
=======================

.. c:type:: struct ubi_eba_leb_desc

    EBA logical eraseblock descriptor

.. _`ubi_eba_leb_desc.definition`:

Definition
----------

.. code-block:: c

    struct ubi_eba_leb_desc {
        int lnum;
        int pnum;
    }

.. _`ubi_eba_leb_desc.members`:

Members
-------

lnum
    the logical eraseblock number

pnum
    the physical eraseblock where the LEB can be found

.. _`ubi_eba_leb_desc.description`:

Description
-----------

This structure is here to hide EBA's internal from other part of the
UBI implementation.

One can query the position of a LEB by calling \ :c:func:`ubi_eba_get_ldesc`\ .

.. _`ubi_volume`:

struct ubi_volume
=================

.. c:type:: struct ubi_volume

    UBI volume description data structure.

.. _`ubi_volume.definition`:

Definition
----------

.. code-block:: c

    struct ubi_volume {
        struct device dev;
        struct cdev cdev;
        struct ubi_device *ubi;
        int vol_id;
        int ref_count;
        int readers;
        int writers;
        int exclusive;
        int metaonly;
        int reserved_pebs;
        int vol_type;
        int usable_leb_size;
        int used_ebs;
        int last_eb_bytes;
        long long used_bytes;
        int alignment;
        int data_pad;
        int name_len;
        char name[UBI_VOL_NAME_MAX + 1];
        int upd_ebs;
        int ch_lnum;
        long long upd_bytes;
        long long upd_received;
        void *upd_buf;
        struct ubi_eba_table *eba_tbl;
        unsigned int checked:1;
        unsigned int corrupted:1;
        unsigned int upd_marker:1;
        unsigned int updating:1;
        unsigned int changing_leb:1;
        unsigned int direct_writes:1;
    }

.. _`ubi_volume.members`:

Members
-------

dev
    device object to make use of the the Linux device model

cdev
    character device object to create character device

ubi
    reference to the UBI device description object

vol_id
    volume ID

ref_count
    volume reference count

readers
    number of users holding this volume in read-only mode

writers
    number of users holding this volume in read-write mode

exclusive
    whether somebody holds this volume in exclusive mode

metaonly
    whether somebody is altering only meta data of this volume

reserved_pebs
    how many physical eraseblocks are reserved for this volume

vol_type
    volume type (%UBI_DYNAMIC_VOLUME or \ ``UBI_STATIC_VOLUME``\ )

usable_leb_size
    logical eraseblock size without padding

used_ebs
    how many logical eraseblocks in this volume contain data

last_eb_bytes
    how many bytes are stored in the last logical eraseblock

used_bytes
    how many bytes of data this volume contains

alignment
    volume alignment

data_pad
    how many bytes are not used at the end of physical eraseblocks to
    satisfy the requested alignment

name_len
    volume name length

name
    volume name

upd_ebs
    how many eraseblocks are expected to be updated

ch_lnum
    LEB number which is being changing by the atomic LEB change
    operation

upd_bytes
    how many bytes are expected to be received for volume update or
    atomic LEB change

upd_received
    how many bytes were already received for volume update or
    atomic LEB change

upd_buf
    update buffer which is used to collect update data or data for
    atomic LEB change

eba_tbl
    EBA table of this volume (LEB->PEB mapping)

checked
    %1 if this static volume was checked

corrupted
    %1 if the volume is corrupted (static volumes only)

upd_marker
    %1 if the update marker is set for this volume

updating
    %1 if the volume is being updated

changing_leb
    %1 if the atomic LEB change ioctl command is in progress

direct_writes
    %1 if direct writes are enabled for this volume

.. _`ubi_volume.description`:

Description
-----------

The \ ``corrupted``\  field indicates that the volume's contents is corrupted.
Since UBI protects only static volumes, this field is not relevant to
dynamic volumes - it is user's responsibility to assure their data
integrity.

The \ ``upd_marker``\  flag indicates that this volume is either being updated at
the moment or is damaged because of an unclean reboot.

.. _`ubi_volume_desc`:

struct ubi_volume_desc
======================

.. c:type:: struct ubi_volume_desc

    UBI volume descriptor returned when it is opened.

.. _`ubi_volume_desc.definition`:

Definition
----------

.. code-block:: c

    struct ubi_volume_desc {
        struct ubi_volume *vol;
        int mode;
    }

.. _`ubi_volume_desc.members`:

Members
-------

vol
    reference to the corresponding volume description object

mode
    open mode (%UBI_READONLY, \ ``UBI_READWRITE``\ , \ ``UBI_EXCLUSIVE``\ 
    or \ ``UBI_METAONLY``\ )

.. _`ubi_debug_info`:

struct ubi_debug_info
=====================

.. c:type:: struct ubi_debug_info

    debugging information for an UBI device.

.. _`ubi_debug_info.definition`:

Definition
----------

.. code-block:: c

    struct ubi_debug_info {
        unsigned int chk_gen:1;
        unsigned int chk_io:1;
        unsigned int chk_fastmap:1;
        unsigned int disable_bgt:1;
        unsigned int emulate_bitflips:1;
        unsigned int emulate_io_failures:1;
        unsigned int emulate_power_cut:2;
        unsigned int power_cut_counter;
        unsigned int power_cut_min;
        unsigned int power_cut_max;
        char dfs_dir_name[UBI_DFS_DIR_LEN + 1];
        struct dentry *dfs_dir;
        struct dentry *dfs_chk_gen;
        struct dentry *dfs_chk_io;
        struct dentry *dfs_chk_fastmap;
        struct dentry *dfs_disable_bgt;
        struct dentry *dfs_emulate_bitflips;
        struct dentry *dfs_emulate_io_failures;
        struct dentry *dfs_emulate_power_cut;
        struct dentry *dfs_power_cut_min;
        struct dentry *dfs_power_cut_max;
    }

.. _`ubi_debug_info.members`:

Members
-------

chk_gen
    if UBI general extra checks are enabled

chk_io
    if UBI I/O extra checks are enabled

chk_fastmap
    if UBI fastmap extra checks are enabled

disable_bgt
    disable the background task for testing purposes

emulate_bitflips
    emulate bit-flips for testing purposes

emulate_io_failures
    emulate write/erase failures for testing purposes

emulate_power_cut
    emulate power cut for testing purposes

power_cut_counter
    count down for writes left until emulated power cut

power_cut_min
    minimum number of writes before emulating a power cut

power_cut_max
    maximum number of writes until emulating a power cut

dfs_dir_name
    name of debugfs directory containing files of this UBI device

dfs_dir
    direntry object of the UBI device debugfs directory

dfs_chk_gen
    debugfs knob to enable UBI general extra checks

dfs_chk_io
    debugfs knob to enable UBI I/O extra checks

dfs_chk_fastmap
    debugfs knob to enable UBI fastmap extra checks

dfs_disable_bgt
    debugfs knob to disable the background task

dfs_emulate_bitflips
    debugfs knob to emulate bit-flips

dfs_emulate_io_failures
    debugfs knob to emulate write/erase failures

dfs_emulate_power_cut
    debugfs knob to emulate power cuts

dfs_power_cut_min
    debugfs knob for minimum writes before power cut

dfs_power_cut_max
    debugfs knob for maximum writes until power cut

.. _`ubi_device`:

struct ubi_device
=================

.. c:type:: struct ubi_device

    UBI device description structure

.. _`ubi_device.definition`:

Definition
----------

.. code-block:: c

    struct ubi_device {
        struct cdev cdev;
        struct device dev;
        int ubi_num;
        char ubi_name[sizeof(UBI_NAME_STR)+5];
        int vol_count;
        struct ubi_volume *volumes[UBI_MAX_VOLUMES+UBI_INT_VOL_COUNT];
        spinlock_t volumes_lock;
        int ref_count;
        int image_seq;
        int rsvd_pebs;
        int avail_pebs;
        int beb_rsvd_pebs;
        int beb_rsvd_level;
        int bad_peb_limit;
        int autoresize_vol_id;
        int vtbl_slots;
        int vtbl_size;
        struct ubi_vtbl_record *vtbl;
        struct mutex device_mutex;
        int max_ec;
        int mean_ec;
        unsigned long long global_sqnum;
        spinlock_t ltree_lock;
        struct rb_root ltree;
        struct mutex alc_mutex;
        int fm_disabled;
        struct ubi_fastmap_layout *fm;
        struct ubi_fm_pool fm_pool;
        struct ubi_fm_pool fm_wl_pool;
        struct rw_semaphore fm_eba_sem;
        struct rw_semaphore fm_protect;
        void *fm_buf;
        size_t fm_size;
        struct work_struct fm_work;
        int fm_work_scheduled;
        int fast_attach;
        struct rb_root used;
        struct rb_root erroneous;
        struct rb_root free;
        int free_count;
        struct rb_root scrub;
        struct list_head pq[UBI_PROT_QUEUE_LEN];
        int pq_head;
        spinlock_t wl_lock;
        struct mutex move_mutex;
        struct rw_semaphore work_sem;
        int wl_scheduled;
        struct ubi_wl_entry **lookuptbl;
        struct ubi_wl_entry *move_from;
        struct ubi_wl_entry *move_to;
        int move_to_put;
        struct list_head works;
        int works_count;
        struct task_struct *bgt_thread;
        int thread_enabled;
        char bgt_name[sizeof(UBI_BGT_NAME_PATTERN)+2];
        long long flash_size;
        int peb_count;
        int peb_size;
        int bad_peb_count;
        int good_peb_count;
        int corr_peb_count;
        int erroneous_peb_count;
        int max_erroneous;
        int min_io_size;
        int hdrs_min_io_size;
        int ro_mode;
        int leb_size;
        int leb_start;
        int ec_hdr_alsize;
        int vid_hdr_alsize;
        int vid_hdr_offset;
        int vid_hdr_aloffset;
        int vid_hdr_shift;
        unsigned int bad_allowed:1;
        unsigned int nor_flash:1;
        int max_write_size;
        struct mtd_info *mtd;
        void *peb_buf;
        struct mutex buf_mutex;
        struct mutex ckvol_mutex;
        struct ubi_debug_info dbg;
    }

.. _`ubi_device.members`:

Members
-------

cdev
    character device object to create character device

dev
    UBI device object to use the the Linux device model

ubi_num
    UBI device number

ubi_name
    UBI device name

vol_count
    number of volumes in this UBI device

volumes
    volumes of this UBI device

volumes_lock
    protects \ ``volumes``\ , \ ``rsvd_pebs``\ , \ ``avail_pebs``\ , beb_rsvd_pebs,
    \ ``beb_rsvd_level``\ , \ ``bad_peb_count``\ , \ ``good_peb_count``\ , \ ``vol_count``\ ,
    \ ``vol``\ ->readers, \ ``vol``\ ->writers, \ ``vol``\ ->exclusive,
    \ ``vol``\ ->metaonly, \ ``vol``\ ->ref_count, \ ``vol``\ ->mapping and
    \ ``vol``\ ->eba_tbl.

ref_count
    count of references on the UBI device

image_seq
    image sequence number recorded on EC headers

rsvd_pebs
    count of reserved physical eraseblocks

avail_pebs
    count of available physical eraseblocks

beb_rsvd_pebs
    how many physical eraseblocks are reserved for bad PEB
    handling

beb_rsvd_level
    normal level of PEBs reserved for bad PEB handling

bad_peb_limit
    top limit of expected bad physical eraseblocks

autoresize_vol_id
    ID of the volume which has to be auto-resized at the end
    of UBI initialization

vtbl_slots
    how many slots are available in the volume table

vtbl_size
    size of the volume table in bytes

vtbl
    in-RAM volume table copy

device_mutex
    protects on-flash volume table and serializes volume
    creation, deletion, update, re-size, re-name and set
    property

max_ec
    current highest erase counter value

mean_ec
    current mean erase counter value

global_sqnum
    global sequence number

ltree_lock
    protects the lock tree and \ ``global_sqnum``\ 

ltree
    the lock tree

alc_mutex
    serializes "atomic LEB change" operations

fm_disabled
    non-zero if fastmap is disabled (default)

fm
    in-memory data structure of the currently used fastmap

fm_pool
    in-memory data structure of the fastmap pool

fm_wl_pool
    in-memory data structure of the fastmap pool used by the WL
    sub-system

fm_eba_sem
    allows \ :c:func:`ubi_update_fastmap`\  to block EBA table changes

fm_protect
    serializes \ :c:func:`ubi_update_fastmap`\ , protects \ ``fm_buf``\  and makes sure
    that critical sections cannot be interrupted by \ :c:func:`ubi_update_fastmap`\ 

fm_buf
    vmalloc()'d buffer which holds the raw fastmap

fm_size
    fastmap size in bytes

fm_work
    fastmap work queue

fm_work_scheduled
    non-zero if fastmap work was scheduled

fast_attach
    non-zero if UBI was attached by fastmap

used
    RB-tree of used physical eraseblocks

erroneous
    RB-tree of erroneous used physical eraseblocks

free
    RB-tree of free physical eraseblocks

free_count
    Contains the number of elements in \ ``free``\ 

scrub
    RB-tree of physical eraseblocks which need scrubbing

pq
    protection queue (contain physical eraseblocks which are temporarily
    protected from the wear-leveling worker)

pq_head
    protection queue head

wl_lock
    protects the \ ``used``\ , \ ``free``\ , \ ``pq``\ , \ ``pq_head``\ , \ ``lookuptbl``\ , \ ``move_from``\ ,
    \ ``move_to``\ , \ ``move_to_put``\  \ ``erase_pending``\ , \ ``wl_scheduled``\ , \ ``works``\ ,
    \ ``erroneous``\ , \ ``erroneous_peb_count``\ , \ ``fm_work_scheduled``\ , \ ``fm_pool``\ ,
    and \ ``fm_wl_pool``\  fields

move_mutex
    serializes eraseblock moves

work_sem
    used to wait for all the scheduled works to finish and prevent
    new works from being submitted

wl_scheduled
    non-zero if the wear-leveling was scheduled

lookuptbl
    a table to quickly find a \ :c:type:`struct ubi_wl_entry <ubi_wl_entry>`\  object for any
    physical eraseblock

move_from
    physical eraseblock from where the data is being moved

move_to
    physical eraseblock where the data is being moved to

move_to_put
    if the "to" PEB was put

works
    list of pending works

works_count
    count of pending works

bgt_thread
    background thread description object

thread_enabled
    if the background thread is enabled

bgt_name
    background thread name

flash_size
    underlying MTD device size (in bytes)

peb_count
    count of physical eraseblocks on the MTD device

peb_size
    physical eraseblock size

bad_peb_count
    count of bad physical eraseblocks

good_peb_count
    count of good physical eraseblocks

corr_peb_count
    count of corrupted physical eraseblocks (preserved and not
    used by UBI)

erroneous_peb_count
    count of erroneous physical eraseblocks in \ ``erroneous``\ 

max_erroneous
    maximum allowed amount of erroneous physical eraseblocks

min_io_size
    minimal input/output unit size of the underlying MTD device

hdrs_min_io_size
    minimal I/O unit size used for VID and EC headers

ro_mode
    if the UBI device is in read-only mode

leb_size
    logical eraseblock size

leb_start
    starting offset of logical eraseblocks within physical
    eraseblocks

ec_hdr_alsize
    size of the EC header aligned to \ ``hdrs_min_io_size``\ 

vid_hdr_alsize
    size of the VID header aligned to \ ``hdrs_min_io_size``\ 

vid_hdr_offset
    starting offset of the volume identifier header (might be
    unaligned)

vid_hdr_aloffset
    starting offset of the VID header aligned to
    \ ``hdrs_min_io_size``\ 

vid_hdr_shift
    contains \ ``vid_hdr_offset``\  - \ ``vid_hdr_aloffset``\ 

bad_allowed
    whether the MTD device admits bad physical eraseblocks or not

nor_flash
    non-zero if working on top of NOR flash

max_write_size
    maximum amount of bytes the underlying flash can write at a
    time (MTD write buffer size)

mtd
    MTD device descriptor

peb_buf
    a buffer of PEB size used for different purposes

buf_mutex
    protects \ ``peb_buf``\ 

ckvol_mutex
    serializes static volume checking when opening

dbg
    debugging information for this UBI device

.. _`ubi_ainf_peb`:

struct ubi_ainf_peb
===================

.. c:type:: struct ubi_ainf_peb

    attach information about a physical eraseblock.

.. _`ubi_ainf_peb.definition`:

Definition
----------

.. code-block:: c

    struct ubi_ainf_peb {
        int ec;
        int pnum;
        int vol_id;
        int lnum;
        unsigned int scrub:1;
        unsigned int copy_flag:1;
        unsigned long long sqnum;
        union {
            struct rb_node rb;
            struct list_head list;
        } u;
    }

.. _`ubi_ainf_peb.members`:

Members
-------

ec
    erase counter (%UBI_UNKNOWN if it is unknown)

pnum
    physical eraseblock number

vol_id
    ID of the volume this LEB belongs to

lnum
    logical eraseblock number

scrub
    if this physical eraseblock needs scrubbing

copy_flag
    this LEB is a copy (@copy_flag is set in VID header of this LEB)

sqnum
    sequence number

u
    unions RB-tree or \ ``list``\  links

u.rb
    link in the per-volume RB-tree of \ :c:type:`struct ubi_ainf_peb <ubi_ainf_peb>`\  objects

u.list
    link in one of the eraseblock lists

.. _`ubi_ainf_peb.description`:

Description
-----------

One object of this type is allocated for each physical eraseblock when
attaching an MTD device. Note, if this PEB does not belong to any LEB /
volume, the \ ``vol_id``\  and \ ``lnum``\  fields are initialized to \ ``UBI_UNKNOWN``\ .

.. _`ubi_ainf_volume`:

struct ubi_ainf_volume
======================

.. c:type:: struct ubi_ainf_volume

    attaching information about a volume.

.. _`ubi_ainf_volume.definition`:

Definition
----------

.. code-block:: c

    struct ubi_ainf_volume {
        int vol_id;
        int highest_lnum;
        int leb_count;
        int vol_type;
        int used_ebs;
        int last_data_size;
        int data_pad;
        int compat;
        struct rb_node rb;
        struct rb_root root;
    }

.. _`ubi_ainf_volume.members`:

Members
-------

vol_id
    volume ID

highest_lnum
    highest logical eraseblock number in this volume

leb_count
    number of logical eraseblocks in this volume

vol_type
    volume type

used_ebs
    number of used logical eraseblocks in this volume (only for
    static volumes)

last_data_size
    amount of data in the last logical eraseblock of this
    volume (always equivalent to the usable logical eraseblock
    size in case of dynamic volumes)

data_pad
    how many bytes at the end of logical eraseblocks of this volume
    are not used (due to volume alignment)

compat
    compatibility flags of this volume

rb
    link in the volume RB-tree

root
    root of the RB-tree containing all the eraseblock belonging to this
    volume (&struct ubi_ainf_peb objects)

.. _`ubi_ainf_volume.description`:

Description
-----------

One object of this type is allocated for each volume when attaching an MTD
device.

.. _`ubi_attach_info`:

struct ubi_attach_info
======================

.. c:type:: struct ubi_attach_info

    MTD device attaching information.

.. _`ubi_attach_info.definition`:

Definition
----------

.. code-block:: c

    struct ubi_attach_info {
        struct rb_root volumes;
        struct list_head corr;
        struct list_head free;
        struct list_head erase;
        struct list_head alien;
        struct list_head fastmap;
        int corr_peb_count;
        int empty_peb_count;
        int alien_peb_count;
        int bad_peb_count;
        int maybe_bad_peb_count;
        int vols_found;
        int highest_vol_id;
        int is_empty;
        int force_full_scan;
        int min_ec;
        int max_ec;
        unsigned long long max_sqnum;
        int mean_ec;
        uint64_t ec_sum;
        int ec_count;
        struct kmem_cache *aeb_slab_cache;
        struct ubi_ec_hdr *ech;
        struct ubi_vid_io_buf *vidb;
    }

.. _`ubi_attach_info.members`:

Members
-------

volumes
    root of the volume RB-tree

corr
    list of corrupted physical eraseblocks

free
    list of free physical eraseblocks

erase
    list of physical eraseblocks which have to be erased

alien
    list of physical eraseblocks which should not be used by UBI (e.g.,
    those belonging to "preserve"-compatible internal volumes)

fastmap
    list of physical eraseblocks which relate to fastmap (e.g.,
    eraseblocks of the current and not yet erased old fastmap blocks)

corr_peb_count
    count of PEBs in the \ ``corr``\  list

empty_peb_count
    count of PEBs which are presumably empty (contain only
    0xFF bytes)

alien_peb_count
    count of PEBs in the \ ``alien``\  list

bad_peb_count
    count of bad physical eraseblocks

maybe_bad_peb_count
    count of bad physical eraseblocks which are not marked
    as bad yet, but which look like bad

vols_found
    number of volumes found

highest_vol_id
    highest volume ID

is_empty
    flag indicating whether the MTD device is empty or not

force_full_scan
    flag indicating whether we need to do a full scan and drop

min_ec
    lowest erase counter value

max_ec
    highest erase counter value

max_sqnum
    highest sequence number value

mean_ec
    mean erase counter value

ec_sum
    a temporary variable used when calculating \ ``mean_ec``\ 

ec_count
    a temporary variable used when calculating \ ``mean_ec``\ 

aeb_slab_cache
    slab cache for \ :c:type:`struct ubi_ainf_peb <ubi_ainf_peb>`\  objects

ech
    temporary EC header. Only available during scan

vidb
    *undescribed*

.. _`ubi_attach_info.description`:

Description
-----------

This data structure contains the result of attaching an MTD device and may
be used by other UBI sub-systems to build final UBI data structures, further
error-recovery and so on.

.. _`ubi_work`:

struct ubi_work
===============

.. c:type:: struct ubi_work

    UBI work description data structure.

.. _`ubi_work.definition`:

Definition
----------

.. code-block:: c

    struct ubi_work {
        struct list_head list;
        int (*func)(struct ubi_device *ubi, struct ubi_work *wrk, int shutdown);
        struct ubi_wl_entry *e;
        int vol_id;
        int lnum;
        int torture;
        int anchor;
    }

.. _`ubi_work.members`:

Members
-------

list
    a link in the list of pending works

func
    worker function

e
    physical eraseblock to erase

vol_id
    the volume ID on which this erasure is being performed

lnum
    the logical eraseblock number

torture
    if the physical eraseblock has to be tortured

anchor
    produce a anchor PEB to by used by fastmap

.. _`ubi_work.description`:

Description
-----------

The \ ``func``\  pointer points to the worker function. If the \ ``shutdown``\  argument is
not zero, the worker has to free the resources and exit immediately as the
WL sub-system is shutting down.
The worker has to return zero in case of success and a negative error code in
case of failure.

.. _`ubi_init_vid_buf`:

ubi_init_vid_buf
================

.. c:function:: void ubi_init_vid_buf(const struct ubi_device *ubi, struct ubi_vid_io_buf *vidb, void *buf)

    Initialize a VID buffer

    :param const struct ubi_device \*ubi:
        the UBI device

    :param struct ubi_vid_io_buf \*vidb:
        the VID buffer to initialize

    :param void \*buf:
        the underlying buffer

.. _`ubi_alloc_vid_buf`:

ubi_alloc_vid_buf
=================

.. c:function:: struct ubi_vid_io_buf *ubi_alloc_vid_buf(const struct ubi_device *ubi, gfp_t gfp_flags)

    Allocate a VID buffer

    :param const struct ubi_device \*ubi:
        the UBI device

    :param gfp_t gfp_flags:
        GFP flags to use for the allocation

.. _`ubi_free_vid_buf`:

ubi_free_vid_buf
================

.. c:function:: void ubi_free_vid_buf(struct ubi_vid_io_buf *vidb)

    Free a VID buffer

    :param struct ubi_vid_io_buf \*vidb:
        the VID buffer to free

.. _`ubi_get_vid_hdr`:

ubi_get_vid_hdr
===============

.. c:function:: struct ubi_vid_hdr *ubi_get_vid_hdr(struct ubi_vid_io_buf *vidb)

    Get the VID header attached to a VID buffer

    :param struct ubi_vid_io_buf \*vidb:
        VID buffer

.. _`ubi_ro_mode`:

ubi_ro_mode
===========

.. c:function:: void ubi_ro_mode(struct ubi_device *ubi)

    switch to read-only mode.

    :param struct ubi_device \*ubi:
        UBI device description object

.. _`vol_id2idx`:

vol_id2idx
==========

.. c:function:: int vol_id2idx(const struct ubi_device *ubi, int vol_id)

    get table index by volume ID.

    :param const struct ubi_device \*ubi:
        UBI device description object

    :param int vol_id:
        volume ID

.. _`idx2vol_id`:

idx2vol_id
==========

.. c:function:: int idx2vol_id(const struct ubi_device *ubi, int idx)

    get volume ID by table index.

    :param const struct ubi_device \*ubi:
        UBI device description object

    :param int idx:
        table index

.. _`ubi_is_fm_vol`:

ubi_is_fm_vol
=============

.. c:function:: bool ubi_is_fm_vol(int vol_id)

    check whether a volume ID is a Fastmap volume.

    :param int vol_id:
        volume ID

.. _`ubi_find_fm_block`:

ubi_find_fm_block
=================

.. c:function:: struct ubi_wl_entry *ubi_find_fm_block(const struct ubi_device *ubi, int pnum)

    check whether a PEB is part of the current Fastmap.

    :param const struct ubi_device \*ubi:
        UBI device description object

    :param int pnum:
        physical eraseblock to look for

.. _`ubi_find_fm_block.description`:

Description
-----------

This function returns a wear leveling object if \ ``pnum``\  relates to the current
fastmap, \ ``NULL``\  otherwise.

.. This file was automatic generated / don't edit.

