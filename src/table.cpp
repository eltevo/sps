#include "table.h"

double& table::operator()(size_t i, size_t j)
{
    return container[i + j * rows ];
}

double table::operator()(size_t i, size_t j) const
{
    return container[i + j * rows ];
}
