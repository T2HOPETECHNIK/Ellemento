import {Entity, model, property} from '@loopback/repository';

@model({settings: {strict: false}})
export class LightHistory extends Entity {
  @property({
    type: 'number',
    id: true,
    generated: true,
  })
  light_history_id?: number;

  @property({
    type: 'number',
    required: true,
  })
  location_id: number;

  @property({
    type: 'number',
    required: true,
  })
  light_status: number;

  @property({
    type: 'number',
    required: true,
  })
  light_level: number;

  @property({
    type: 'number',
  })
  batch_id?: number;

  @property({
    type: 'date',
    required: true,
  })
  date_time: string;

  @property({
    type: 'number',
  })
  locationId?: number;
  // Define well-known properties here

  // Indexer property to allow additional data
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  [prop: string]: any;

  constructor(data?: Partial<LightHistory>) {
    super(data);
  }
}

export interface LightHistoryRelations {
  // describe navigational properties here
}

export type LightHistoryWithRelations = LightHistory & LightHistoryRelations;
