set(TemplateSrc Template.cpp)
add_library(Template STATIC ${TemplateSrc})
install(TARGETS Template)
#add_library(Template SHARED ${TemplateSrc})
