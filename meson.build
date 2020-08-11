project('hellomeson', 'c')

cc = meson.get_compiler('c')

lib_files = ['lib/a.c',
              'lib/b.c']
custom_c_args = []
if get_option('optimize-gc-sections') and cc.has_argument('-fdata-sections')
  custom_c_args += ['-fdata-sections', '-ffunction-sections']
endif


# generate a static archive
hello_lib = static_library('static-hello-lib',
                lib_files,
                c_args: custom_c_args
                )
library_args = []
mapfile = 'public_symbols.lds'
# Generate a linker script if `stripped-symbols` is passed to meson args
if get_option('stripped-symbols') != ''
  all_symbol_names = get_option('stripped-symbols')
  generate_init_linker_script = find_program('scripts/generate_linker_script.py')
  init_static_plugins_c = configure_file(
    output: mapfile,
  command : [generate_init_linker_script,
             '@OUTPUT@',
             all_symbol_names]
  )
  library_args += ['-Wl,--version-script=public_symbols.lds']
endif

# collect dead symbols from sections
library_args += ['-Wl,--gc-sections']

# create the dynamic library from the static archive with the symbols stripped
library('hello-lib',
        link_whole: hello_lib,
        link_args: library_args,
        link_depends:  meson.current_build_dir() + '/' + mapfile
        )

executable('hello-meson',
            'src/hello.c',
            link_with: hello_lib,
            link_args: ['-Wl,--gc-sections']
            )
