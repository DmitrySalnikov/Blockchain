/// @file block.h
/// @brief описание блока

#ifndef MATHCYB2020_BLOCK_H
#define MATHCYB2020_BLOCK_H

#include <string>
#include <ctime>

class Block
{
private:
    uint64_t nounce; // параметр proof-of-work
    time_t timestamp; // время создания блока
    uint64_t hash; // хэш предыдущего блока, либо 0 для первого блока

protected:
    std::string message; // данные, хранящиеся в блоке

public:
    /// @brief конструктор по умолчанию
    Block();

    /// @brief констурктор с параметрами, устанавливающий параметр времени создания timestamp
    /// @param nounce параметр proof-of-work
    /// @param hash хэш предыдущего блока, либо 0 для первого блока
    /// @param message данные, хранящиеся в блоке
    Block( const uint64_t nounce, const uint64_t hash, const std::string message );

    /// @brief конструктор копирования
    /// @param ссылка на копируемый блок
    Block( const Block &block );

    /// @brief деструктор
    ~Block();
};

#endif //MATHCYB2020_BLOCK_H
