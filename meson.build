project('hellomeson', 'c')

cc = meson.get_compiler('c')

lib_files = ['lib/a.c',
              'lib/b.c']


hello_lib = static_library('hello-lib',
                lib_files,
                c_args: ['-fdata-sections', '-ffunction-sections'])

executable('hello-meson',
            'src/hello.c',
            link_with: hello_lib,
            link_args: ['-Wl,--gc-sections']
            )
