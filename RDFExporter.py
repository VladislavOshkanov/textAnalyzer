def build_cs_array(predicates):
    """
    Создаёт массив констант-ситуаций, входящих в атомарную диаграмму
    :param predicates: двухместные предикаты
    :return: список констант-ситуаций
    """

    cs_set = set()
    for predicate in predicates:
        cs_set.add(predicate.constant_situation)

    return cs_set


def export_to_rdf(predicates, hypothesis):
    """
    Экспортирует извлечённые предикаты в формате RDF
    :param predicates: двухместные предикаты
    :param hypothesis: извлечённые гипотезы
    """

    xml_version = "1.0"
    rdf_schema_url = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    t2t_prefix= "t2t"
    t2t_schema_url = ""

    cs_set = build_cs_array(predicates)

    rdf = ''

    rdf += "<?xml version=\""
    rdf += xml_version
    rdf += "\"?>\n\n"

    rdf += "<rdf:RDF "
    rdf += "xmlns:rdf=\""
    rdf += rdf_schema_url
    rdf += "\" "

    rdf += "xmlns:"
    rdf += t2t_prefix
    rdf += "=\""
    rdf += t2t_schema_url
    rdf += "\">\n\n"

    for cs in cs_set:
        rdf += "<rdf:Description rdf:about=\""
        rdf += "S" + str(cs)
        rdf += "\">\n"
        for predicate in predicates:
            if predicate.constant_situation == cs:
                rdf += "\t<"
                rdf += t2t_prefix
                rdf += ":"
                rdf += predicate.name.replace(" ", "_")
                rdf += ">"
                rdf += predicate.value
                rdf += "</"
                rdf += t2t_prefix
                rdf += ":"
                rdf += predicate.name.replace(" ", "_")
                rdf += ">\n"

        for h in hypothesis:
            if h.first_cs == cs:
                rdf += "\t<"
                rdf += t2t_prefix
                rdf += ":"
                rdf += h.name
                rdf += ">"
                rdf += "S" + str(h.second_cs)
                rdf += "</"
                rdf += t2t_prefix
                rdf += ":"
                rdf += h.name
                rdf += ">\n"
        rdf += "</rdf:Description>\n\n"

    rdf += "</rdf:RDF>\n"

    f = open("out.xml", "w")
    f.write(rdf)
    f.close()

    print(rdf)

