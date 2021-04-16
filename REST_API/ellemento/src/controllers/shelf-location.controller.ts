import {
  Count,
  CountSchema,
  Filter,
  repository,
  Where,
} from '@loopback/repository';
import {
  del,
  get,
  getModelSchemaRef,
  getWhereSchemaFor,
  param,
  patch,
  post,
  requestBody,
} from '@loopback/rest';
import {
  Shelf,
  Location,
} from '../models';
import {ShelfRepository} from '../repositories';

export class ShelfLocationController {
  constructor(
    @repository(ShelfRepository) protected shelfRepository: ShelfRepository,
  ) { }

  @get('/shelves/{id}/locations', {
    responses: {
      '200': {
        description: 'Array of Shelf has many Location',
        content: {
          'application/json': {
            schema: {type: 'array', items: getModelSchemaRef(Location)},
          },
        },
      },
    },
  })
  async find(
    @param.path.number('id') id: number,
    @param.query.object('filter') filter?: Filter<Location>,
  ): Promise<Location[]> {
    return this.shelfRepository.locations(id).find(filter);
  }

  @post('/shelves/{id}/locations', {
    responses: {
      '200': {
        description: 'Shelf model instance',
        content: {'application/json': {schema: getModelSchemaRef(Location)}},
      },
    },
  })
  async create(
    @param.path.number('id') id: typeof Shelf.prototype.shelf_id,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(Location, {
            title: 'NewLocationInShelf',
            exclude: ['location_id'],
            optional: ['shelfId']
          }),
        },
      },
    }) location: Omit<Location, 'location_id'>,
  ): Promise<Location> {
    return this.shelfRepository.locations(id).create(location);
  }

  @patch('/shelves/{id}/locations', {
    responses: {
      '200': {
        description: 'Shelf.Location PATCH success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async patch(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(Location, {partial: true}),
        },
      },
    })
    location: Partial<Location>,
    @param.query.object('where', getWhereSchemaFor(Location)) where?: Where<Location>,
  ): Promise<Count> {
    return this.shelfRepository.locations(id).patch(location, where);
  }

  @del('/shelves/{id}/locations', {
    responses: {
      '200': {
        description: 'Shelf.Location DELETE success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async delete(
    @param.path.number('id') id: number,
    @param.query.object('where', getWhereSchemaFor(Location)) where?: Where<Location>,
  ): Promise<Count> {
    return this.shelfRepository.locations(id).delete(where);
  }
}
